
from celery import Celery
app = Celery("task",
             include=["Tasks"],
             broker='pyamqp://worker:worker@localhost:5672/')


