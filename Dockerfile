# pull official base image
FROM python:3.9.17-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev postgresql-client
RUN apk add --no-cache --virtual .pynacl_deps build-base libffi-dev

COPY . /usr/src/app/

# install dependencies
RUN pip3 install --upgrade pip
# RUN pip install -r requirements.txt 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install


# move manage.py to the working directory
COPY manage.py /usr/src/app/manage.py