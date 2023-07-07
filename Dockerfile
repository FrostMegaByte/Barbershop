FROM nvcr.io/nvidia/pytorch:20.12-py3
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/src/app

# Needed for cv2 to work
RUN apt-get update -y && apt-get install ffmpeg libsm6 libxext6 -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

ENTRYPOINT [ "python", "app.py" ]