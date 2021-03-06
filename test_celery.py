#! env bin/python
# codding = utf-8

from celery import Celery

# app = Celery('hello', broker='amqp://guest@localhost//')

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    return 'hello world'