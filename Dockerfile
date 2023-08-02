# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

COPY . /usr/src/app/

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install


# move manage.py to the working directory
COPY manage.py /usr/src/app/manage.py

# Collect static files
RUN python manage.py collectstatic --noinput
