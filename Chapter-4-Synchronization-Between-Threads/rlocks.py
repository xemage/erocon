import threading
import time

class myWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.Rlock = threading.RLock()

    def modifyA(self):
        with self.Rlock:
            print("Modifying A : RLock Acquired: {0}".format(self.Rlock._is_owned()))
            print("{0}".format(self.Rlock))
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.Rlock:
            print("Modifying B : RLock Acquired: {0}".format(self.Rlock._is_owned()))
            print("{0}".format(self.Rlock))
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.Rlock:
            print("Rlock acquired, modifying A and B")
            print("{0}".format(self.Rlock))
            self.modifyA()
            print("{0}".format(self.Rlock))
            self.modifyB()
            print("{0}".format(self.Rlock))
        print("{0}".format(self.Rlock))

workerA = myWorker()
workerA.modifyBoth()