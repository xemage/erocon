# Thankfully, within Python, we can actually map all the elements of an iterator to a function,
# and submit these as independent jobs to our ThreadPoolExecutor:
# results = executor.map(multiplyByTwo, values)
# This, essentially, saves us from doing something far more verbose like the following
# example:
# for value in values:
#   executor.submit(multiplyByTwo, (value))

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

values = [2,3,4,5,6,7,8,'a']

def multiplyByTwo(n):
    return 2 * n

def main():
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiplyByTwo, values)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()