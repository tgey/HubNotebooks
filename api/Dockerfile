FROM python:3.6

RUN mkdir -p /home/project/app
WORKDIR /home/project/app

# copy and install packages for flask
COPY requirements.txt /home/project/app
RUN pip install --no-cache-dir -r requirements.txt

# copy contents from your local to your docker container
COPY . /home/project/app
# COPY ./models /home/project/app/models
# COPY ./api /home/project/app/api

#EXPOSE 8000

# ENV ENVIRONMENT production

# ENTRYPOINT [ "python", "api/main.py" ]