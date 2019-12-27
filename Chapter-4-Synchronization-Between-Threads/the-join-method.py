import threading
import time

def ourThread(i):
    print("Thread {0} Started".format(i))
    time.sleep(i*2)
    print("Thread {0} Finished".format(i))

def main():
    thread1 = threading.Thread(target=ourThread, args=(1,))
    thread1.start()
    print("Is thread 1 Finished?")
    thread2 = threading.Thread(target=ourThread, args=(2,))
    thread2.start()
    thread2.join() # wait with join() until thread is finished
    print("Thread 2 definitely finished")

if __name__ == '__main__':
    main()