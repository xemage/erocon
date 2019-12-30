# Pass in priority_number as the first value in tuple: (priority_number, data).

import threading
import queue
import random
import time

def mySubscriber(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()
        time.sleep(1)

myQueue = queue.PriorityQueue()
for i in range(5):
    myQueue.put(i, i) # (priority_number, data)

for i in range(5):
    myQueue.put(i, i)

print("Queue Populated")

threads = []
for i in range(2):
    thread = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    
print("Queue is empty")