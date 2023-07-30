# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
# RUN apt install -y libpq-dev 
# RUN apt install -y gcc 

COPY . /usr/src/app/

# install dependencies
RUN pip3 install --upgrade pip
# RUN pip install -r requirements.txt 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install


# move manage.py to the working directory
COPY manage.py /usr/src/app/manage.py