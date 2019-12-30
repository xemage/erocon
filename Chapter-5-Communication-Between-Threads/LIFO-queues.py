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
        queue.task_done()
        time.sleep(0.5)

myQueue = queue.LifoQueue()
for i in range(100):
    myQueue.put(i)
    print("{0} added to queue".format(i))
print("Queue Populated")

threads = []
for i in range(5):
    thread = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Queue is empty")