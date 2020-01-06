#from timer import Timer
import time
from urllib.request import Request, urlopen
import ssl

from timeit import default_timer

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = default_timer
        self.elapsed = 0
        
    def __enter__(self):
        self.start = default_timer()
        return self
        
    def __exit__(self, *args):
        end = default_timer()
        self.elapsed = end - self.start
        if self.verbose:
            print("Time taken to execute function: {}".format(self.elapsed))

def myFunction():
    # We create this context so that we can crawl
    # https sites
    myssl = ssl.create_default_context()
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    with Timer() as t:
        print("Starting request")
        import pdb; pdb.set_trace() # <-- Python debugger breakpoint
        req = Request('https://tutorialedge.net', headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=myssl)
    
    print("Elapsed Time: {} seconds".format(t.elapsed))

if __name__ == "__main__":
    myFunction()