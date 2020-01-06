import threading
from urllib.request import Request, urlopen, urljoin, URLError
from urllib.parse import urlparse
from queue import Queue
from bs4 import BeautifulSoup
import ssl
import time

# A queue with an additional set to hold all items ever processed
# When an item is put it is checked if the item was processed before /
# it is in the set all_items
# Queue methods are thread safe, thus no additional locks needed
class SetQueue(Queue):

    def _init(self, maxsize):
        Queue._init(self, maxsize) 
        self.all_items = set() # to keep track of all processed items

    def _put(self, item):
        if item not in self.all_items:
            Queue._put(self, item) 
            self.all_items.add(item)
        else:
            print("Queue - Not a new item: {0}".format(item))


class Crawler(threading.Thread):

    def __init__(self, baseUrl, linksToCrawl, finished):
        threading.Thread.__init__(self)
        print("Web Crawler thread started: {0}".format(self.name))      
        self.linksToCrawl = linksToCrawl
        self.baseUrl = baseUrl
        self.baseNetloc = urlparse(baseUrl).netloc
        self.finished = finished
        print("Thread name: {0} - Base url: {1} - Base netloc: {2}".format(self.name, self.baseUrl, self.baseNetloc))

    def run(self):
        # Create context so that we can crawl https sites
        myssl = ssl.create_default_context()
        myssl.check_hostname=False
        myssl.verify_mode=ssl.CERT_NONE

        # process all the links in queue
        while not self.finished.is_set():
            try:
      
                print("Crawler thread: {0} - Queue Size: {1}".format(self.name, self.linksToCrawl.qsize()))
                link = self.linksToCrawl.get()

                # have we reached the end of our queue?
                if link is None:
                    print("Thread: {0} - Queue is empty.".format(self.name))
                    continue
                else:
                    print("Thread: {0} - Current link from queue: {1}".format(self.name, link))
        
                    try:
                        print("Thread: {0} - Joining base url {1} and link {2}".format(self.name, self.baseUrl, link))
                        link = urljoin(self.baseUrl, link) # this should work for non absolute links
                        print("Thread: {0} - Joined link is: {1}".format(self.name, link))

                        print("Thread: {0} - Current link to crawl: {1}".format(self.name, link))
                        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                        response = urlopen(req, context=myssl)

                        print("Thread: {0} - Url requested: {1}".format(self.name, response.geturl()))
                        print("Thread: {0} - Status: {1}".format(self.name, response.getcode()))
                
                        soup = BeautifulSoup(response.read(), "html.parser")
                
                        for atag in soup.find_all('a'):
                            href = atag.get('href')
                            print("Thread: {0} - Current href: {1}".format(self.name, href))

                            if href == None:
                                print("Thread: {0} - No href found for atag: {1}".format(self.name, atag))
                                continue
                            else:
                                print("Thread: {0} - href found for atag: {1}".format(self.name, atag))

                            # get netloc
                            netloc = urlparse(href).netloc
                            print("Thread: {0} - netloc of href is: {1}".format(self.name, netloc))

                            # if netloc is empty string
                            #   it's a relative link -> add base url -> add to links to crawl
                            # if netloc is not empty
                            #   if netloc == baseNetloc -> add to links to crawl
                            #   else -> external link -> don't crawl
                            if netloc == '':
                                absLink = urljoin(link, href)
                                print("Thread: {0} - Adding link to linksToCrawl: {1}".format(self.name, absLink))
                                self.linksToCrawl.put(absLink)
                            else:
                                if netloc == self.baseNetloc:
                                    absLink = href
                                    print("Thread: {0} - Adding link to linksToCrawl: {1}".format(self.name, absLink))
                                    self.linksToCrawl.put(absLink)
                                else:
                                    # external link
                                    print("Thread: {0} - External or broken link: {1}".format(self.name, href))
                                    pass

                        print("Thread: {0} - Finished crawling link: {1}".format(self.name, link))
                        #self.haveVisited.add(link)
                
                    except Exception as e:
                        print("Thread: {0} - Error during thread execution: {2}".format(self.name, link, e.reason))
            finally:
                self.linksToCrawl.task_done()

def queue_observer(oberserved_queue, finished, max_empty_time = 30, max_runtime = 240):
    start_time = time.time()
    time_not_empty = time.time()
    runtime = 0
    seconds_empty = 0
    
    while not finished.is_set():

        if oberserved_queue.empty():            
            seconds_empty = time.time() - time_not_empty          
            print("Observer - Queue is empty since {0} seconds".format(seconds_empty))
        else:
            seconds_empty = 0
            time_not_empty = time.time()

        if seconds_empty > max_empty_time:
            print("Observer - Queue is empty since more than {0} seconds. Setting finished flag".format(max_empty_time))
            finished.set()

        if runtime > max_runtime:
            print("Maximum runtime of {0} reached. Setting finished flag".format(max_runtime))
            finished.set()

        runtime = time.time() - start_time
        time.sleep(1)


def main():
    print("Starting Web Crawler")
    baseUrl = input("Website > ")
    numberOfThreads = int(input("Number of threads > "))
    max_runtime = int(input("Maximum runtime in seconds > "))

    finished_flag = threading.Event()

    linksToCrawl = SetQueue()    
    linksToCrawl.put(baseUrl)


    crawlers = []
    

    for i in range(numberOfThreads):
        crawler = Crawler(baseUrl, linksToCrawl, finished_flag)
        crawler.daemon = True
        crawler.start()
        crawlers.append(crawler)    

    observer = threading.Thread(target=queue_observer, args=(linksToCrawl, finished_flag, 30, max_runtime))
    observer.start()

    for crawler in crawlers:
        crawler.join(timeout=5.0)
    print("Crawler threads joined")
    observer.join()
    print("Observer joined")

    print("Total Number of Pages Visited {}".format(len(linksToCrawl.all_items)))

    # Write visited links to file
    with open('visited links.txt', 'w') as f:
        for link in linksToCrawl.all_items:
            f.write("{0}\n".format(link))

if __name__ == '__main__':
    main()