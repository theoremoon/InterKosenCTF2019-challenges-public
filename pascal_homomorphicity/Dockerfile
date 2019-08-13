FROM python:3.7-alpine

RUN apk --no-cache add socat
RUN apk add gcc g++ make libffi-dev openssl-dev
RUN pip3 install pycryptodome

COPY ./challenge/secrets.py /secrets.py
COPY ./challenge/service.py /service.py

CMD socat TCP-L:8888,fork,reuseaddr EXEC:"python service.py"
