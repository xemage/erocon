import time
import threading
from urllib.request import Request, URLError, urljoin, urlopen
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [
'http://localhost:1313',
'http://localhost:1313/about',
'http://localhost:1313/get-involved/',
'http://localhost:1313/series/blog/',
]

def checkStatus(url):
    print("Thread {} attempting to crawl URL: {}".format(threading.currentThread(), url))
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.getcode(), url

def printStatus(statusCode):
    print("URL Crawled with status code: {}".format(statusCode))

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = []
        for url in URLS:
            task = executor.submit(checkStatus, (url))
            tasks.append(task)
        
        for result in as_completed(tasks):
            printStatus(result)

if __name__ == '__main__':
    main()