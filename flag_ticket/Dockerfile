FROM python:3.7

COPY ./challenge/Pipfile /
COPY ./challenge/Pipfile.lock /
RUN pip install pipenv && pipenv install --system
COPY ./challenge /

CMD uvicorn main:api --host "0.0.0.0" --port 80

