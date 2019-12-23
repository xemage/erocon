# Example that highlights the non-deterministic behavior of the task scheduler
# The code also shows one of the dangers of multiple threads accessing shared resources without any form of synchronization

import threading
import time
import random
from pynput import keyboard

# Global signals
exit_signal = threading.Event() # global exit signal
counter = 1

def workerA():
    global counter
    print('... workerA starting ...')
    while not exit_signal.is_set():
        if counter < 100:
            counter += 1
            print("Worker A is incrementing counter to {0}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)

    return False

def workerB():
    global counter
    print('... workerB starting ...')
    while not exit_signal.is_set():
        if counter > -100:
            counter -= 1
            print("Worker B is decrementing counter to {0}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)

    return False

# keyboard handling
def on_key_release(key):

    if key == keyboard.Key.esc:
        print('... Shutdown request ...')
        # set exit_signal
        exit_signal.set()

def main():
    t0 = time.time()

    print('... Press <ESC> to shutdown ...')

    keyboardListener = keyboard.Listener(on_release = on_key_release)

    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)

    keyboardListener.start()
    thread1.start()
    thread2.start()

    # Keep alive main thread
    try:
        while not exit_signal.is_set():
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    print('... Shutting down ...')
    keyboardListener.stop()

    keyboardListener.join(3.0) # timeout after x seconds
    thread1.join(3.0) # timeout after x seconds
    thread2.join(3.0) # timeout after x seconds    

    t1 = time.time()
    print("Execution Time {0}".format(t1-t0))

if __name__ == '__main__':
    main()