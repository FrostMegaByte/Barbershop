import os
os.environ["MKL_THREADING_LAYER"] = "GNU"

import dlib
from pathlib import Path
import argparse
import torchvision
import PIL

from utils.drive import open_url
from utils.shape_predictor import align_face

parser = argparse.ArgumentParser(description="Align_face")

# fmt: off
parser.add_argument('-unprocessed_dir', type=str, default='unprocessed', help='directory with unprocessed images')
parser.add_argument('-output_dir', type=str, default='input', help='output directory')

parser.add_argument('-output_size', type=int, default=1024, help='size to downscale the input images to, must be power of 2')
parser.add_argument('-seed', type=int, help='manual seed to use')
parser.add_argument('-cache_dir', type=str, default='cache', help='cache directory for model weights')

parser.add_argument('-inter_method', type=str, default='bicubic')
# fmt: on


args = parser.parse_args()

cache_dir = Path(args.cache_dir)
cache_dir.mkdir(parents=True, exist_ok=True)

unprocessed_dir = Path(args.unprocessed_dir)

output_dir = Path(args.output_dir)
output_dir.mkdir(parents=True, exist_ok=True)

f = open_url(
    "https://drive.google.com/uc?id=1huhv8PYpNNKbGCLOaYUjOgR1pY5pmbJx",
    cache_dir=cache_dir,
    return_path=True,
)
predictor = dlib.shape_predictor(f)

for im in Path(args.unprocessed_dir).glob("*.*"):
    if im.name == ".gitkeep":
        continue
    if os.path.exists(f"{output_dir}/{im.stem}.png"):
        print(f"{im.stem} was already aligned")
        os.remove(im)
        continue
    
    faces = align_face(str(im), predictor)

    for i, face in enumerate(faces):
        if args.output_size:
            factor = 1024 // args.output_size
            assert args.output_size * factor == 1024
            face_tensor = torchvision.transforms.ToTensor()(face).unsqueeze(0).cuda()
            face_tensor_lr = face_tensor[0].cpu().detach().clamp(0, 1)
            face = torchvision.transforms.ToPILImage()(face_tensor_lr)
            if factor != 1:
                face = face.resize(
                    (args.output_size, args.output_size), PIL.Image.LANCZOS
                )
        if len(faces) > 1:
            face.save(output_dir / (im.stem + f"_{i}.png"))
        else:
            face.save(output_dir / (im.stem + f".png"))
        os.remove(im)
