# Image-Upload

# Dependensies
1. django
2. pillow

# Deployment -- Docker File
FROM Ubuntu

RUN apt-get update
RUN apt-install python

RUN pip install django
RUN pip install pillow

COPY ./opt/source-code

ENTRYPOINT DJANGO_APP = /opt/source-code/app.py run django

# How to Deploy
1. Build the Docker File above.
2. Push the image to the docker hub repository.
3. Containerize the image of the application and deploy it to the server.
NB: Make sure that the ports are propered wired so that the containers is listening on the ports that the intended users can access.

