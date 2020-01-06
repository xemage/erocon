# To benchmark with cProfile run this python file with
# python -m cProfile advanced-cprofile-example.py
#
# The output will show the following
# ncalls: This is the number of times a line/function is called throughout the execution of our program.
# tottime: This is the total time that the line or function took to execute.
# percall: This is the total time divided by the number of calls.
# cumtime: This is the cumulative time spent executing this line or function.
# percall: This is the quotient of cumtime divided by the number of primitive calls.
# filename: lineno(function): This represents the actual line or function that we are measuring.

import threading
import random
import time

def myWorker():
    for i in range(5):
        print("Starting wait time")
        time.sleep(random.randint(1,5))
        print("Completed Wait")

def main():
    thread1 = threading.Thread(target=myWorker)
    thread2 = threading.Thread(target=myWorker)
    thread3 = threading.Thread(target=myWorker)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()