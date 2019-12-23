# Download ten images sequentially
# from lorempixel which will deliver a different image each call

import urllib.request
import time
from pathlib import Path

def downloadImage(url, file):
    print("Downloading Image from ", url)
    urllib.request.urlretrieve(url, file)

def main():
    t0 = time.time()

    for i in range(10):             
        image_path = Path("temp/image-{0}.jpg".format(str(i)))
        downloadImage("http://lorempixel.com/400/200/sports", image_path)

    # calculate the total execution time
    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution Time {}".format(totalTime))

if __name__ == '__main__':
    main()