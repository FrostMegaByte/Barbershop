# Barbershop: GAN-based Image Compositing using Segmentation Masks
![teaser](docs/assets/webapp.png)

## Original work
> [**Barbershop: GAN-based Image Compositing using Segmentation Masks**](https://zpdesu.github.io/Barbershop/)<br/>
[Peihao Zhu](https://github.com/ZPdesu),
[Rameen Abdal](https://github.com/RameenAbdal),
[John Femiani](https://scholar.google.com/citations?user=rS1xJIIAAAAJ&hl=en),
[Peter Wonka](http://peterwonka.net/)<br/>

> [arXiv](https://arxiv.org/abs/2106.01505) | [BibTeX](#bibtex) | [Project Page](https://zpdesu.github.io/Barbershop/) | [Video](https://youtu.be/ZU-yrAvoJfQ)

## Forked code
> [Mark Bekooy](https://github.com/FrostMegaByte)


## Installation
- **You need to have a Nvidia GPU. Otherwise this project doesn't work...**
- Clone the repository:
``` 
git clone https://github.com/FrostMegaByte/Barbershop.git
cd Barbershop
```
- Dependencies:  
We recommend running this repository using [Docker](https://docs.docker.com/engine/install/).  
All dependencies for defining the environment from the original repository were based on conda. These are provided in `environment/environment.yml`.  
**However**, creating the Docker image from the Dockerfile and running that as a container is much easier.


### Optional - Hairstyle inspiration
For hairstyle inspiration, see [II2S](https://drive.google.com/drive/folders/15jsR9yy_pfDHiS9aE3HcYDgwtBbAneId?usp=sharing) which you can download.


## Getting Started  
1. Make sure that you have a Nvidia GPU!
2. Build the docker image:
```
docker build -t barbershop .
```

3. (a) Run the docker image as a container OR:
```
docker run --gpus all -it -d -p 8080:7860 barbershop
```

3. (b) Run the docker image as a container with mounted volume (if you want to see the resulting hairstyle files on your own system):
```
docker run --gpus all -it -d -p 8080:7860 -v <absolute_local_path>:/usr/src/app barbershop
```

4. Start the webapp by going to `localhost:8080` and uploading your images.

5. Wait for ~20 minutes to generate the new hairstyle. _(Depending on your GPU. Mine was a GTX 1070TI)_

6. Optional - Want to access the bash shell of the container?
```
docker ps -a
docker exec -it <container_id> /bin/bash
```
