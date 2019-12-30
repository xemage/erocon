# Queues, by default, are thread safe in Python

import threading
import queue
import random
import time

def mySubscriber(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print("{0} removed {1} from the queue".format(threading.current_thread(), item))
        # Indicate that a formerly enqueued task is complete. 
        # Used by queue consumer threads. For each get() used to fetch a task, 
        # a subsequent call to task_done() tells the queue that the processing on the task is complete.
        queue.task_done()
        time.sleep(1)

myQueue = queue.Queue()
for i in range(10):
    myQueue.put(i)
print("Queue Populated")
print(myQueue)

threads = []
for i in range(4):
    thread = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()