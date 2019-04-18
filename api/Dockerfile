FROM python:3.6

RUN mkdir -p /home/api
WORKDIR /home/api

COPY requirements.txt /home/api
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api /home/api
