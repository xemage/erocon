from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import threading
import random

def isEven(n):
    print("Thread {} checking if {} is even".format(threading.currentThread(), n))
    if type(n) != int:
        raise Exception("Value entered is not an integer")
    if n % 2 == 0:
        print("Thread {} - {} is even".format(threading.currentThread(), n))
        return True
    else:
        print("Thread {} - {} is odd".format(threading.currentThread(), n))
        return False

def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        task1 = executor.submit(isEven, (2))
        task2 = executor.submit(isEven, (3))
        task3 = executor.submit(isEven, ('t'))
    
    for future in concurrent.futures.as_completed([task1, task2, task3]):        
        print("Result of Task: {}".format(future.result()))

if __name__ == '__main__':
    main()

# You should see the results of the tasks printing out followed by the exception thrown
# by the third task’s invalid input