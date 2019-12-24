import os

def child():
    print("We are in the child process with PID={0}".format(os.getpid()))

def parent():
    print("We are in the parent process with PID={0}".format(os.getpid()))
    newRef=os.getpid()

    if newRef==0:
        child()
    else:
        print("We are in the parent process and our child process has PID={0}".format(newRef))

parent()