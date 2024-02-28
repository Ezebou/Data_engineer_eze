FROM python:3.12.2

COPY . usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python main.py   
