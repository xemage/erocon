# Kernprof comes with the line_profiler tool, by default, and allows us to easily get
# started using the line_profiler tool. With line_profiler, we need to explicitly state
# the functions that we need to profile within our codebase. This is typically done using the
# @profile decorator.

# If we wanted a line-by-line analysis of exactly how long everything takes, then we can add
# the @profile decorator to the function we want to analyze.

# In order to run the analyzis tool, we first have to call the kernprof tool in order to generate an
# .lprof file. It’s this file that we’ll be passing into our
# line_profiler tool in order to see the exact output.

# analyze every line line: python -m kernprof -l kernprof-example.py
# analyze every line and show results: python -m kernprof -l -v kernprof-example.py

import random
import time

@profile # Decorator for Kernprof
def slowFunction():
    time.sleep(random.randint(1,5))     # <-- test should show that this line is the most time consuming
    print("Slow Function Executed")

@profile # Decorator for Kernprof
def fastFunction():
    print("Fast Function Executed")

@profile # Decorator for Kernprof
def main():
    slowFunction()
    fastFunction()

if __name__ == '__main__':
    main()