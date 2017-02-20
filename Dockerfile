FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install virtualenv
RUN virtualenv .virtualenv
ENV PATH /code/.virtualenv/bin:$PATH
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code
