# Cancelling tasks submitted to an executor can be done by calling the cancel() function on that specific task.
# The cancel function returns a boolean value which is either true if we successfully managed
# to cancel the future object, or false if unsuccessful. In the preceding example, you would see
# that it returns false unless you submit jobs prior to myTask that keeps the executor object
# occupied.

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
        task3 = executor.submit(someTask, (3))
        task4 = executor.submit(someTask, (4))
        print("Canceling task 3 - result: {}".format(task3.cancel()))

if __name__ == '__main__':
    main()