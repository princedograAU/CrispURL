FROM python:3.8.2-alpine3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /gateway
WORKDIR /gateway

# install build  dependencies
#RUN apk update
#RUN apk upgrade
#RUN apk add --no-cache gcc
#RUN apk add --no-cache libffi-dev
#RUN apk add --no-cache postgresql-client
#RUN apk add --update --no-cache --virtual .tmp-build-deps libc-dev linux-headers
#RUN apk add --no-cache postgresql-dev
#RUN apk add --no-cache musl-dev
RUN apk add --upgrade --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

# setup pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /gateway/
RUN  pip install pipenv  \
    && pipenv lock --keep-outdated --requirements > requirements.txt \
    && pip install -r requirements.txt

COPY ./gateway /gateway

#add user for security purposes
RUN adduser -D user
USER user
