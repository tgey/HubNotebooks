FROM nikolaik/python-nodejs:latest

WORKDIR /home/jupyterlab

COPY requirements.txt /home/jupyterlab

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN jupyter labextension install @jupyterlab/google-drive

COPY . /home/jupyterlab

CMD jupyter lab --port=8888 --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password=''