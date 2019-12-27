# This example will get stucked waiting for the lock to get unlocked
# and is a good example of when to use RLocks

import threading
import time

class myWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.Lock()

    def modifyA(self):
        with self.lock:
            print("Modifying A : RLock Acquired: {0}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.lock:
            print("Modifying B : Lock Acquired: {0}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.lock:
            print("lock acquired, modifying A and B")
            print("{}".format(self.lock))
            self.modifyA()
            print("{}".format(self.lock))
            self.modifyB()
        print("{}".format(self.lock))

workerA = myWorker()
workerA.modifyBoth()