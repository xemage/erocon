import threading
import time

def myThread():
    print("Thread {} starting".format(threading.currentThread().getName()))
    time.sleep(10)
    print("Thread {} ending".format(threading.currentThread().getName()))

for i in range(4):
    threadName = "Listener-" + str(i)
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()

for i in range(4):
    threadName = "Calculator-" + str(i)
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()

print("{}".format(threading.enumerate()))