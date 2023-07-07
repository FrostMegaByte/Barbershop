FROM nvcr.io/nvidia/pytorch:20.12-py3
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/src/app

# RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g') \
#   && wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb \
#   && dpkg -i cuda-keyring_1.0-1_all.deb

# RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
#   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | apt-key add - \
#   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | tee /etc/apt/sources.list.d/nvidia-docker.list

# RUN apt-get update -y
# RUN apt-get install -y cuda-drivers nvidia-docker2

# Needed for cv2 to work
RUN apt-get update -y && apt-get install ffmpeg libsm6 libxext6 -y

# RUN pip install dlib==19.22.1
# RUN pip install gdown==4.2.0
# RUN pip install scikit-image==0.19.2
# RUN pip install opencv-python==4.5.4.58
# RUN pip install gradio==3.35.2
# RUN pip install pydantic==1.10.11

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

ENTRYPOINT [ "python", "app.py" ]