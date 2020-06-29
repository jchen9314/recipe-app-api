FROM python:3.7-alpine
MAINTAINER JC

# ensure the py output is sent straight to terminal w/o being first buffered
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# for security purpose (user can only run app)
RUN adduser -D user
USER user
