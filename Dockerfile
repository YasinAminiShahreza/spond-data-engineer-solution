FROM ubuntu:22.04
RUN apt update
RUN apt upgrade -y

RUN apt install  python3  python3-pip -y
RUN python3  -m pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Usually you have more control when using base ubuntu images and running and installing
# your own configuration especially for bussiness critical apps

#you can host your image in the github repo or Azure Container Registrey using github 
#actions or devops pipelines and use this as the
# base image for the team. That's what I meant in the Pro tip in the conceptual questions.

# run the image after the built and run Q1.py and Q2.py
#docker run -it spond-test:ubuntu /bin/bash
#cd solution/code 
#python3 Q2.py

# in order to run the docker as seamless development experience, 
# 1 - build the docker image
# 2 - Install the "Remote Developemtn" VS code extension
# 3 - Choose this dockerfile and you're good to go:))