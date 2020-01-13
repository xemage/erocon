import multiprocessing
import time

def myProcess():
    current_process = multiprocessing.current_process()
    print("Child Process PID: {}".format(current_process.pid))
    time.sleep(20)

def main():
    current_process = multiprocessing.current_process()
    print("Main process PID: {}".format(current_process.pid))
    cildyProcess = multiprocessing.Process(target=myProcess)
    cildyProcess.start()
    time.sleep(2)
    print("My Process has terminated, terminating main thread")
    print("Terminating Child Process")
    cildyProcess.terminate()
    print("Child Process Successfully terminated")

if __name__ == '__main__':
    main()