# define a LockedSet class object, which inherits from our traditional Python
# set class. Within the constructor for this class, we create a lock object, which we’ll use in
# subsequent functions in order to allow for thread-safe interactions.

from threading import Lock

class LockedSet(set):
    """A set where add(), remove(), and 'in' operator are thread-safe"""

    # Within the constructor for this class, we create a lock object, which we’ll use in
    # subsequent functions in order to allow for thread-safe interactions.
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
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


x = set([1, 2, 3, 4])
print('--------------- x -------------------')
print('type(x): {0}'.format(type(x)))
print('x: {0}'.format(x))
print('x.__contains__(2): {0}'.format(x.__contains__(2)))
print('2 in x: {0}'.format(2 in x))
print('for elem in x: print(elem)')
for elem in x:
    print(elem)

b = {1, 2, 3, 4}
print('--------------- b -------------------')
print('type(b): {0}'.format(type(b)))
print('b: {0}'.format(b))
print('b.__contains__(2): {0}'.format(b.__contains__(2)))
print('2 in b: {0}'.format(2 in b))
print('for elem in b: print(elem)')
for elem in b:
    print(elem)

y = LockedSet([1, 2, 3, 4])
print('--------------- y -------------------')
print('type(y): {0}'.format(type(y)))
print('y: {0}'.format(y))
print('y.__contains__(2): {0}'.format(y.__contains__(2)))
print('2 in y: {0}'.format(2 in y))
print('for elem in y: print(elem)')
for elem in y:
    print(elem)

z = LockedSet({1, 2, 3, 4})
print('--------------- z -------------------')
print('type(z): {0}'.format(type(z)))
print('z: {0}'.format(z))
print('z.__contains__(2): {0}'.format(z.__contains__(2)))
print('2 in z: {0}'.format(2 in z))
print('for elem in z: print(elem)')
for elem in z:
    print(elem)