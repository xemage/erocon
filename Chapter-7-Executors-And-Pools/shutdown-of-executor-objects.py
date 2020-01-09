# In this example, we are going to demonstrate a shutdown of a running executor. We’ll first
# define a function which will essentially "work" for n number of seconds. We’ll submit a
# number of tasks, and then call the shutdown method on our executor. After this point, we
# will attempt to submit yet more tasks to the executor:

import time
import random
from concurrent.futures import ThreadPoolExecutor

def someTask(n):
    print("Executing Task {}".format(n))
    time.sleep(n)
    print("Task {} Finished Executing".format(n))

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(someTask, (1))
        task2 = executor.submit(someTask, (2))
        executor.shutdown(wait=True)
        task3 = executor.submit(someTask, (3))
        task4 = executor.submit(someTask, (4))

if __name__ == '__main__':
    main()

# you should see a runtime error when runningthis script