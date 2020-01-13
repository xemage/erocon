import multiprocessing

def myProcess():
    print("Currently Executing Child Process")
    print("This process has it's own instance of the GIL")

def main():
    print("Executing Main Process")
    print("Creating Child Process")
    childProcess = multiprocessing.Process(target=myProcess)
    childProcess.start()
    childProcess.join()
    print("Child Process has terminated, terminating main process")

if __name__ == "__main__":
    main()