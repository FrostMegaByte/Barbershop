import os
import gradio as gr
import subprocess
import PIL
import hashlib

def process_images(personal_image, hairstyle_image, haircolor_image):
    def hash(image):
        return hashlib.sha256(image.tobytes()).hexdigest()[:12]
    
    personal_image_name = f"personal_{hash(personal_image)}"
    hairstyle_image_name = f"hairstyle_{hash(hairstyle_image)}"
    haircolor_image_name = f"haircolor_{hash(haircolor_image)}"
    
    current_directory = os.path.dirname(os.path.realpath(__file__))
    personal_image.save(os.path.join(current_directory, "unprocessed", f"{personal_image_name}.png"))
    hairstyle_image.save(os.path.join(current_directory, "unprocessed", f"{hairstyle_image_name}.png"))
    haircolor_image.save(os.path.join(current_directory, "unprocessed", f"{haircolor_image_name}.png"))
    
    # Preprocess user submitted images
    print("[1] Starting preprocessing faces for alignment...")
    subprocess.run(["python", "align_face.py"])
    
    # Generate hairstyle
    print("\n[2] Starting hairstyle generation...")
    subprocess.run(["python", "main.py", "--im_path1", f"{personal_image_name}.png", "--im_path2", f"{hairstyle_image_name}.png", "--im_path3", f"{haircolor_image_name}.png", "--sign", "realistic", "--smooth", "5"])
    
    result_image = PIL.Image.open(f"output/{personal_image_name}_{hairstyle_image_name}_{haircolor_image_name}_realistic.png")

    return result_image

with gr.Blocks() as demo:
    gr.Markdown("# Barbershop - Hairstyle Generator")
    gr.Markdown("Upload 3 images and wait for ~10 minutes")
    with gr.Row():
        with gr.Column():
            personal_image_input = gr.Image(label="Photo of yourself", type="pil")
            hairstyle_image_input = gr.Image(label="Hairstyle photograph", type="pil")
            haircolor_image_input = gr.Image(label="Haircolor photograph", type="pil")
            image_button = gr.Button("Generate Hairstyle!")
        with gr.Column():
            image_output = gr.Image(label="Result")

    image_button.click(process_images, inputs=[personal_image_input, hairstyle_image_input, haircolor_image_input], outputs=image_output)

demo.launch()