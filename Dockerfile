FROM python:alpine3.10
WORKDIR /app
COPY ./app/app.py /app
RUN apk add curl
RUN pip3 install --upgrade pip
RUN pip3 install flask
EXPOSE 8888
CMD python3 ./app.py
