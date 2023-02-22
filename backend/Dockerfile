FROM python:3.11-slim

WORKDIR /notenapp-backend

COPY ./. /notenapp-backend
COPY requirements.txt /notenapp-backend

RUN apt upgrade

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 /notenapp-backend/main.py