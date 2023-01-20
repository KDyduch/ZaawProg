FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

ENV HOST=0.0.0.0
ENV PORT=80

CMD src.app.login.Login:app --host=${HOST} --port=${PORT}
