# syntax=docker/dockerfile:1
FROM python:3.9.5-alpine

# creates workdir
WORKDIR /app

# set flask env vars
ENV FLASK_APP=app.py
ENV FLASK_RUN=0.0.0.0
ENV FLASK_ENV=development

# install required unix libs
RUN apk add --no-cache gcc musl-dev linux-headers

# copy requirements to container and pip install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# exposes port 5000 to be acessed from outside
EXPOSE 5000

# copy database creator script to /tmp/
COPY ./db/createDatabase.py /tmp/

# creates data directory. Our DB files will live here.
RUN mkdir /data

# create and seed the database
RUN python3 /tmp/createDatabase.py

# default command to run the api
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
