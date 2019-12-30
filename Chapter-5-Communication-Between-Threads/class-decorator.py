# The lock_class function at the start takes in a list of methods and lockfactory, and returns a
# lambda function which takes in the method names specified in the decorator as well as
# lockFactory (i.e. Lock or RLock).

from threading import Lock

def lock_class(methodnames, lockfactory):
    return lambda cls: make_threadsafe(cls, methodnames, lockfactory)

def lock_method(method):
    # Check if the attribute named __is_locked is True
    # and return False if the attribute doesn't exist
    if getattr(method, '__is_locked', False):
        raise TypeError("Method %r is already locked!" %method)

    def locked_method(self, *arg, **kwarg):
        with self._lock:
            return method(self, *arg, **kwarg)
    
    locked_method.__name__ = '%s(%s)' %  ('lock_method', method.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_threadsafe(cls, methodnames, lockfactory):
    # Get original class constructor
    init = cls.__init__
    
    # New class constructor = old class constructor plus lock
    def newinit(self, *arg, **kwarg):
        init(self, *arg, **kwarg)
        self._lock = lockfactory()
    
    # Replace class constructor with locked one
    cls.__init__ = newinit
    
    # Add lock to each method in variable methodnames
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)

    return cls

# Example decoration
# Add lock to constructor (init) and methods 'add' and 'remove'
@lock_class(['add','remove'], Lock)
class ClassDecoratorLockedSet(set):
    @lock_method # if you double-lock a method, a TypeError is raised
    def lockedMethod(self):
        print("This section of our code would be thread safe")


a = ClassDecoratorLockedSet({1, 2, 3, 4})
a.add(5)
print(a)