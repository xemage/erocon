# Use maxsize parameter of queues

import threading
import queue
import time

def myPublisher(queue):
    while not queue.full():
        queue.put(1)
        print("{} Appended 1 to queue: {}".format(threading.current_thread(), queue.qsize()))
        time.sleep(1)

myQueue = queue.Queue(maxsize=25)

threads = []
for i in range(4):
    thread = threading.Thread(target=myPublisher, args=(myQueue,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()