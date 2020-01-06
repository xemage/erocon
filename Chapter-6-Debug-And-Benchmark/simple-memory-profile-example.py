# Test how much memory is used with memory_profiler
# Run analyzis with 
# python -m memory_profiler simple-memory-profile-example.py

import random
import time

@profile
def slowFunction():
    time.sleep(random.randint(1,5))
    print("Slow Function Executed")

@profile
def fastFunction():
    print("Fast Function Executed")

@profile
def main():
    slowFunction()
    fastFunction()

if __name__ == '__main__':
    main()