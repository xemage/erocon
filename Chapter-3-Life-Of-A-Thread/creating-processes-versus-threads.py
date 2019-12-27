import threading
from multiprocessing import Process
import time
import os

def MyTask(number, task_type):
    print("Starting {0} number {1}".format(task_type, number))
    time.sleep(2)

def main():
    t0 = time.time()

    # Create 10 threads
    threads = []
    for i in range(10):
        thread = threading.Thread(target=MyTask, args=("Thread", i,))
        thread.start()
        threads.append(thread)

    t1 = time.time()
    print("Total time for creating 10 Threads: {0} seconds".format(t1-t0))

    time.sleep(5)
    for thread in threads:
        thread.join()

    time.sleep(10)

    t2 = time.time()

    # Create 10 processes
    procs = []
    for i in range(10):
        process = Process(target=MyTask, args=("Process", i,))
        process.start()
        procs.append(process)

    t3 = time.time()
    print("Total time for creating 10 Processes: {0} seconds".format(t3-t2))

    time.sleep(10)

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    main()