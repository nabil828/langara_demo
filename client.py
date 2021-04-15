import logging

from celery import Celery

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

app = Celery('tasks', broker='redis://localhost/',  backend='redis://localhost/') 

# For fibo_tasks
input_list = [4, 3, 8, 6, 10]


def manage_fibo_task(value_list):
    async_result_dict = {x: app.send_task('tasks.fibo_task',
                                          args=(x,), queue='fibo_queue', routing_key='fibo_queue')
                         for x in value_list}

    for key, value in async_result_dict.items():
        if value.ready():
            logger.info("Value [%d] -> %s" % (key, value.get(timeout=5444)[1]))
        else:
            logger.info("The task [%s] is not ready" % value.task_id)

manage_fibo_task(input_list)

