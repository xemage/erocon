from concurrent.futures import ProcessPoolExecutor
import os
import time

def task(n):
    print("Process {} processing {}".format(os.getpid(), n))
    time.sleep(5)
    print("Process {} finished".format(os.getpid()))

def main():
    numbers = [2, 3, 4, 5, 6, 7, 8]
    
    print("Starting ProcessPoolExecutor")
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        """
        future = executor.submit(task, (2))
        future = executor.submit(task, (3))
        future = executor.submit(task, (4))
        future = executor.submit(task, (5))
        future = executor.submit(task, (6))
        future = executor.submit(task, (7))
        """
        future = executor.map(task, numbers)        
    
    print("All tasks complete")

if __name__ == '__main__':
    main()