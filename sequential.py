# coding: utf-8

import logging, threading

from queue import Queue
import random
import time


# Returns the new average
# after including x
def getAvg(prev_avg, x, n):
    return (
            (prev_avg * n + x) /
            (n + 1)
    )


input_list = []
for i in range(100):
    input_list.append(random.randint(20, 30))


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


# Starting the time
start = time.time()
# print("Here we go:")
for i in input_list:
    fibonacci(i)

# stop the time
end = time.time()
diff = end - start
# avg = getAvg(avg, diff, x)
print("Diff: [%s]" % diff)


# print("avg: [%s] " % avg)
