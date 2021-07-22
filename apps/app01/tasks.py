from django_redis.celery import app
from celery import shared_task
import time

# 专属于myproject项目的任务
@app.task
def test():
    pass

@shared_task
def add(x, y):
    with open('text.txt') as f:
        time.sleep(20)
    print(x)
    return x + y