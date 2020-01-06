# THIS CODE IS NOT WORKING PROPERLY!

from urllib.request import Request, urlopen, urljoin, URLError
from urllib.parse import urlparse
import time
import threading
import queue
from bs4 import BeautifulSoup
import ssl

class Crawler(threading.Thread):

    def __init__(self, baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock, hrefs):
        threading.Thread.__init__(self)
        print("Web Crawler Worker Started: {0}".format(threading.current_thread()))        
        self.linksToCrawl = linksToCrawl
        self.haveVisited = haveVisited
        self.baseUrl = baseUrl
        self.baseNetloc = urlparse(baseUrl).netloc
        self.urlLock = urlLock
        self.errorLinks = errorLinks
        self.hrefs = hrefs # implemented for debugging only
        print("Thread name: {0} - Base url: {1} - Base netloc: {2}".format(self.name, self.baseUrl, self.baseNetloc))

    def run(self):
        # We create this context so that we can crawl 
        # https sites
        myssl = ssl.create_default_context();
        myssl.check_hostname=False
        myssl.verify_mode=ssl.CERT_NONE
        # process all the links in our queue
        while True:
      
            self.urlLock.acquire()
            print("Thread: {0} says - Queue Size: {1}".format(self.name, self.linksToCrawl.qsize()))
            link = self.linksToCrawl.get()
            self.urlLock.release()     
            # have we reached the end of our queue?
            if link is None:
                print("Thread: {0} says - Queue is empty.".format(self.name))
                break
            else:
                print("Thread: {0} says - Current link from queue: {1}".format(self.name, link))

            # Have we visited this link already?
            if (link in self.haveVisited):
                print("Thread: {0} says - Already Visited: {1}".format(self.name, link))
                break
      
            try:
                print("Thread: {0} says - Joining base url {1} and link {2}".format(self.name, self.baseUrl, link))
                link = urljoin(self.baseUrl, link) # this should work for non absolute links from queue
                print("Thread: {0} says - Joined link is: {1}".format(self.name, link))
                print("Thread: {0} says - Current link to crawl: {1}".format(self.name, link))
                req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(req, context=myssl)

                print("Thread: {0} says - Url {1} crawled with status: {2}".format(self.name, response.geturl(), response.getcode()))
        
                soup = BeautifulSoup(response.read(), "html.parser")
        
                for atag in soup.find_all('a'):
                    href = atag.get('href')
                    print("Thread: {0} says - Current href: {1}".format(self.name, href))
                    self.hrefs.add(href)

                    # get netloc
                    netloc = urlparse(href).netloc
                    print("Thread: {0} says - netloc of href is: {1}".format(self.name, netloc))

                    # if netloc is empty string
                    #   it's a relative link -> add base url -> add to links to crawl
                    # if netloc is not empty
                    #   if netloc == baseNetloc -> add to links to crawl
                    #   else -> external link -> don't crawl
                    if netloc == '':
                        absLink = urljoin(self.baseUrl, href)
                        print("Thread: {0} says - Adding absLink to linksToCrawl: {1}".format(self.name, absLink))
                        self.linksToCrawl.put(absLink)
                    else:
                        if netloc == self.baseNetloc:
                            absLink = href
                            print("Thread: {0} says - Adding absLink to linksToCrawl: {1}".format(self.name, absLink))
                            self.linksToCrawl.put(absLink)
                        else:
                            # do nothing
                            pass
                    
                    """
                    if (href not in self.haveVisited):
                        print("Thread: {0} says - href not in haveVisited: {1}".format(self.name, href))
                        netloc = urlparse(href).netloc
                        print("Thread: {0} says - netloc of href is: {1}".format(self.name, netloc))
                        if (netloc == self.baseNetloc):
                            print("Thread: {0} says - netloc == baseNetloc".format(self.name))
                            print("Thread: {0} says - Adding href to linksToCrawl: {1}".format(self.name, href))
                            self.linksToCrawl.put(href)
                        else:
                            print("Thread: {0} says - netloc {1} != baseNetloc {2} -> external link".format(self.name, netloc, self.baseNetloc))
                    else :
                        print("Thread: {0} says - Already visited href: {1}".format(self.name, href))
                    """

                print("Thread: {0} says - Adding link to crawled list: {1}".format(self.name, link))
                self.haveVisited.add(link)
        
            except URLError as e:
                print("Thread: {0} says - URL {1} threw this error when trying to parse: {1}".format(self.name, link, e.reason))
                self.errorLinks.add(link)
            finally:
                self.linksToCrawl.task_done()


class LockedSet(set):
    """A set where add(), remove(), and 'in' operator are thread-safe"""

    # Within the constructor for this class, we create a lock object, which we’ll use in
    # subsequent functions in order to allow for thread-safe interactions.
    def __init__(self, *args, **kwargs):
        self._lock = threading.Lock()
        super(LockedSet, self).__init__(*args, **kwargs)

    # Below we define the add, remove, and contains functions. These rely on
    # the super class functionality with one key exception. With each of these functions, we use
    # the lock that we initialized in our constructor to ensure that all interactions can only be
    # executed by one thread at any given time, thus ensuring thread safety.
    def add(self, elem):
        with self._lock:
            super(LockedSet, self).add(elem)
    
    def remove(self, elem):
        with self._lock:
            super(LockedSet, self).remove(elem)
    
    def __contains__(self, elem):
        with self._lock:
            return super(LockedSet, self).__contains__(elem)

def main():
    print("Starting our Web Crawler")
    baseUrl = input("Website > ")
    numberOfThreads = input("Number of threads > ")

    linksToCrawl = queue.Queue()
    urlLock = threading.Lock()
    linksToCrawl.put(baseUrl)
    hrefs = LockedSet()
    haveVisited = LockedSet()
    errorLinks = LockedSet()
    
    crawlers = []
    

    for i in range(int(numberOfThreads)):
        crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock, hrefs)
        crawler.start()
        crawlers.append(crawler)    

    for crawler in crawlers:
        crawler.join()

    print("Total Number of Pages Visited {}".format(len(haveVisited)))
    print("Total Number of Pages with Errors {}".format(len(errorLinks)))

    # Write visited links to file
    with open('visited links.txt', 'w') as f:
        for link in haveVisited:
            f.write("{0}\n".format(link))
    
    # Write error links to file
    with open('error links.txt', 'w') as f:
        for link in errorLinks:
            f.write("{0}\n".format(link))

    # Write hrefs to file
    with open('hrefs.txt', 'w') as f:
        for href in hrefs:
            f.write("{0}\n".format(href))


if __name__ == '__main__':
    main()