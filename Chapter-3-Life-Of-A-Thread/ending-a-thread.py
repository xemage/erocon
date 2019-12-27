# Ending threads is deemed bad practice
# Best practice in stopping threads
# If you require some form of a thread shutdown mechanism, then it is your job to implement
# a mechanism that allows for a graceful shutdown as opposed to killing a thread outright.
# While threads might not possess a native mechanism for termination, processes do

from multiprocessing import Process
import time

def myWorker():
    t1 = time.time()
    print("Process started at: {0}".format(t1))
    time.sleep(20)

myProcess = Process(target=myWorker)
print("Process {0}".format(myProcess))
myProcess.start()
print("Terminating Process...")
myProcess.terminate()
myProcess.join()
print("Process Terminated: {0}".format(myProcess))

# We kick off the process, and then immediately terminate it using the terminate method.
# Notice in the output that this program finishes almost instantly, and the
# myProcess process does not block for the full 20 seconds it was meant to.