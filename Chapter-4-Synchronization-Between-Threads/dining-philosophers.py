import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, name, leftFork, rightFork):
        print("Our philosopher has sat down at the table")
        threading.Thread.__init__(self, name = name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print("Philosopher: {0} has started thinking".format(threading.current_thread().getName()))
        while True:
            time.sleep(random.randint(1,5))
            print("Philosopher {0} has finished thinking".format(threading.current_thread().getName()))
            self.leftFork.acquire()
            time.sleep(random.randint(1,5))
            try:
                print("Philosopher {0} has acquired the left fork".format(threading.current_thread().getName()))
                self.rightFork.acquire()
                try:
                    print("Philosopher {0} has attained both forks, currently eating".format(threading.current_thread().getName()))
                finally:
                    self.rightFork.release()
                    print("Philosopher {0} has released the right fork".format(threading.current_thread().getName()))
            finally:
                self.leftFork.release()
                print("Philosopher {0} has released the left fork".format(threading.current_thread().getName()))


fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = Philosopher("Kant", fork1, fork2)
philosopher2 = Philosopher("Aristotle", fork2, fork3)
philosopher3 = Philosopher("Spinoza", fork3, fork4)
philosopher4 = Philosopher("Marx", fork4, fork5)
philosopher5 = Philosopher("Russell", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()