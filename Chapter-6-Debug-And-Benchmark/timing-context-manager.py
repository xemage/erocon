from timeit import default_timer

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = default_timer
    
    def __enter__(self):
        self.start = default_timer()
        return self
    
    def __exit__(self, *args):
        end = default_timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs
        if self.verbose:
            print('elapsed time: {0} ms'.format(self.elapsed))


from urllib.request import Request, urlopen
import ssl

def myFunction():
    # We create this context so that we can crawl
    # https sites
    myssl = ssl.create_default_context()
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    with Timer() as t:
        req = Request('https://tutorialedge.net', headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=myssl)
    print("Elapsed Time: {0} seconds".format(t.elapsed))

myFunction()