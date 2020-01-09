import threading
from concurrent.futures import ThreadPoolExecutor

def task(n):
    print("Thread {} processing {}".format(threading.currentThread(), n))

def taskDone(fn):
    if fn.cancelled():
        print("Our {} future has been cancelled".format(fn))
    elif fn.done():
        print("Our {} task has completed".format(fn))

def secondTaskDone(fn):
    if fn.cancelled():
        print("Our {} future has been cancelled".format(fn))
    elif fn.done():
        print("Our {} task has completed second task".format(fn))

def main():
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, (2))
        future.add_done_callback(taskDone)

        future2 = executor.submit(task, (3))
        future2.add_done_callback(taskDone)
        future2.add_done_callback(secondTaskDone)
    
    print("All tasks complete")

if __name__ == '__main__':
    main()