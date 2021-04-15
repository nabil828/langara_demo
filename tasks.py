
from celery import Celery
from time import sleep

# app = Celery('tasks', broker='amqps://jdklyhif:FzPxKBCpd_SC6ywjUpezb1uz6f168k7U@beaver.rmq.cloudamqp.com/jdklyhif', backend='db+sqlite:///db.sqlite3') 

app = Celery('tasks', broker='redis://localhost/',  backend='redis://localhost/') 

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]


@app.task
def fibo_task(value):
    a, b = 0, 1
    for item in range(value):
        a, b = b, a + b

    message = "The fibonacci calculated by worker %s was %d" \
              % (fibo_task.request.id, a)
    return (value, message)
