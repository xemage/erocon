from threading import Lock

# This decorator method will define a new method within it and call the original
# method only when it has acquired self._lock.
def locked_method(method):
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return newmethod

class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(DecoratorLockedSet, self).__init__(*args, **kwargs)

    @locked_method
    def add(self, elem):
        return super(DecoratorLockedSet, self).add(elem)

    @locked_method
    def remove(self, elem):
        return super(DecoratorLockedSet, self).remove(elem)


a = DecoratorLockedSet({1, 2, 3, 4})

a.add(5)

print(a)

try:
    a.remove(7)
except:
    print('Ooops')

try:
    a.discard(7)
except:
    print('Oops')

a.discard(3)
print(a)