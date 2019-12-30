# Deques are double-ended queues
# It belongs to the collections module

import collections

doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))

for item in doubleEndedQueue:
    print("Item {}".format(item))

print("Left Most Element: {}".format(doubleEndedQueue[0]))
print("Right Most Element: {}".format(doubleEndedQueue[-1]))

# Appending elements
print("Append 1")
doubleEndedQueue.append('1')
print("Deque: {}".format(doubleEndedQueue))
print("Append left 6")
doubleEndedQueue.appendleft('6')
print("Deque: {}".format(doubleEndedQueue))

# Popping elements
print("Pop")
rightPop = doubleEndedQueue.pop()
print(rightPop)
print("Deque: {}".format(doubleEndedQueue))
print("Pop left")
leftPop = doubleEndedQueue.popleft()
print(leftPop)
print("Deque: {}".format(doubleEndedQueue))

# Inserting elements
print("Insert 5 at position 2")
doubleEndedQueue.insert(2,5)
print("Deque: {}".format(doubleEndedQueue))

# Rotation
print("Rotate 3")
doubleEndedQueue.rotate(3)
print("Deque: {}".format(doubleEndedQueue))
print("Rotate -2 (2 left)")
doubleEndedQueue.rotate(-2)
print("Deque {}".format(doubleEndedQueue))