FROM bitnami/python:3.9 as builder
WORKDIR /home/app
COPY main.py main.py
COPY src src
ENV PYTHONPATH=${PYTHONPATH}:/home/app
ENTRYPOINT ["python", "main.py"]
