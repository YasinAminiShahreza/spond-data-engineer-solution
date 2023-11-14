FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# run the image after the built and run Q1.py and Q2.py
#docker run -it image_name /bin/bash