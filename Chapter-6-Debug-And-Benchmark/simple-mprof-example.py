# Test how much memory is used with mprof
# and show a diagram
# Run analyzis with 
# python -m mprof run simple-mprof-example.py
# This will generate a mprofile_yyyymmddHHMMSS.dat file.
# Show diagram with
# python -m mprof plot mprofile_yyyymmddHHMMSS.dat

import random
import time

def slowFunction():
    time.sleep(random.randint(1,5))
    print("Slow Function Executed")

def fastFunction():
    print("Fast Function Executed")

@profile
def main():
    slowFunction()
    fastFunction()

if __name__ == '__main__':
    main()