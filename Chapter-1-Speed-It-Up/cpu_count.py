# First we import the multiprocessing module
import multiprocessing
# then we call multiprocessing.cpu_count() which
# returns an integer value of how many available CPUs we have
availableCPUs = multiprocessing.cpu_count()

print(availableCPUs)