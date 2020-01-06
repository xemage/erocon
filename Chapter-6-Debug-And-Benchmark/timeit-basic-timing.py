import timeit
import time

def func1():
    print("Function 1 Executing")
    time.sleep(5)
    print("Function 1 complete")

def func2():
    print("Function 2 executing")
    time.sleep(6)
    print("Function 2 complete")

def main():
    start_time = timeit.default_timer()
    func1()
    print(timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    func2()
    print(timeit.default_timer() - start_time)

if __name__ == "__main__":
    main()