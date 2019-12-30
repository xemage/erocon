# The join() function on the queue object allows to block the current thread's execution
# until such point that all elements from the queue have been consumed.

import threading
import queue
import time

def mySubscriber(queue):
    time.sleep(1)
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()

myQueue = queue.Queue()
for i in range(5):
    myQueue.put(i)
print("Queue Populated")

thread = threading.Thread(target=mySubscriber, args=(myQueue,))
thread.start()
print("Not progressing till queue is empty")
myQueue.join() # wait until all elements have been consumed
print("Queue is now empty")