# With events, one thread would, typically, signal that an event
# has occurred while other threads are actively listening for this signal.
#
# An Event has four public functions with which we can modify and utilize it:
# isSet(): This checks to see if the event has been set
# set(): This sets the event
# clear(): This resets our event object
# wait(): This blocks until the internal flag is set to true

import threading
import time

def myThread(myEvent):
    while not myEvent.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("myEvent has been set")

def main():
    myEvent = threading.Event()
    thread1 = threading.Thread(target=myThread, args=(myEvent,))
    thread1.start()
    time.sleep(10)
    myEvent.set()

if __name__ == '__main__':
    main()