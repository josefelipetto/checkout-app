# syntax=docker/dockerfile:1
FROM python:3.9.5-alpine
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN=0.0.0.0
ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./db/createDatabase.py /tmp/
RUN mkdir /data
RUN python3 /tmp/createDatabase.py
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
