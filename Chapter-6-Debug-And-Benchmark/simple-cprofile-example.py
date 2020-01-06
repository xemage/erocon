# To benchmark with cprofile run this python file with
# python -m cProfile simple-cprofile-example.py
#
# The output will show the following
# ncalls: This is the number of times a line/function is called throughout the execution of our program.
# tottime: This is the total time that the line or function took to execute.
# percall: This is the total time divided by the number of calls.
# cumtime: This is the cumulative time spent executing this line or function.
# percall: This is the quotient of cumtime divided by the number of primitive calls.
# filename: lineno(function): This represents the actual line or function that we are measuring.

import collections

doubleEndedQueue = collections.deque('123456')
print("Deque: {}".format(doubleEndedQueue))

doubleEndedQueue.append('1')
print("Deque: {}".format(doubleEndedQueue))

doubleEndedQueue.appendleft('6')
print("Deque: {}".format(doubleEndedQueue))