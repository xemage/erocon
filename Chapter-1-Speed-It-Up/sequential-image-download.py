# Download ten images sequentially
# from lorempixel which will deliver a different image each call

import urllib.request
from pathlib import Path

def downloadImage(url, file):
    print("Downloading Image from ", url)
    urllib.request.urlretrieve(url, file)

def main():
    for i in range(10):             
        image_path = Path("temp/image-{0}.jpg".format(str(i)))
        downloadImage("http://lorempixel.com/400/200/sports", image_path)

if __name__ == '__main__':
    main()