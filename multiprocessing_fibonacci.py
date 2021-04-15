# coding: utf-8

import sys, logging, time, os, random
import time
from multiprocessing import Process, Queue, Pool, \
    cpu_count, current_process, Manager

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


def producer_task(q, fibo_dict):
    for i in range(100):
        value = random.randint(20, 30)
        fibo_dict[value] = None
        # logger.info("Producer [%s] putting value [%d] into queue.. "
        #             % (current_process().name, value))
        q.put(value)


def consumer_task(q, fibo_dict):
    while not q.empty():
        value = q.get(True, 0.05)
        a, b = 0, 1
        for item in range(value):
            # a, b = b, a + b
            fibo_dict[value] = fibonacci(item)
        # logger.info("consumer [%s] getting value [%d] from queue..."
        #             % (current_process().name, value))


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n ==  0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    data_queue = Queue()
    number_of_cpus = cpu_count()
    manager = Manager()
    fibo_dict = manager.dict()

    producer = Process(target=producer_task, args=(data_queue, fibo_dict))
    producer.start()
    producer.join()

    # Starting the time
    start = time.time()
    # print("Here we go")

    consumer_list = []
    for i in range(number_of_cpus):
        consumer = Process(target=consumer_task, args=(data_queue, fibo_dict))
        consumer.start()
        consumer_list.append(consumer)

    [consumer.join() for consumer in consumer_list]

    # stop the time
    end = time.time()
    # print(end - start)
    diff = end - start
    print("Diff: [%s]" % diff)

