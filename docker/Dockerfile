FROM python:3.8.5-slim-buster

ENV PYTHONPATH .

EXPOSE 8000

COPY requirements.txt /retailer/requirements.txt
WORKDIR /retailer
RUN pip install -r requirements.txt

COPY . /retailer

CMD ["bash", "./docker/django_run_server.sh"]
