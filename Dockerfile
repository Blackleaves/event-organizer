FROM python:3.8.5

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN apt-get update
RUN apt-get -y install gcc

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV MYAPP_SETTINGS /usr/src/app/sanic/config.py

CMD ["python","sanic/main.py","--host=0.0.0.0","--port=8000"]
