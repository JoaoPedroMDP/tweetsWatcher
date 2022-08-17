FROM python:3.10

WORKDIR /app
COPY ./app /app

RUN pip install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host", "0.0.0.0"]