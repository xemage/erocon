import sys
import threading
import time
import queue

def myThread(queue):
    exit_thread = False
    
    while exit_thread == False:
        try:
            time.sleep(2)
            raise Exception("Exception Thrown In Child Thread {0}".format(threading.current_thread()))
        except:
            queue.put(sys.exc_info())
            exit_thread = True


def main():
    exception_queue = queue.Queue()
    child_thread = threading.Thread(target=myThread, args=(exception_queue,))
    child_thread.start()

    while True:
        try:
            exception = exception_queue.get()
        except exception_queue.Empty:
            pass
        else:
            print(exception)
            break


if __name__ == "__main__":
    main()