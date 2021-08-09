from timeit import default_timer as timer
from datetime import timedelta
import threading
from multiprocessing.dummy import Pool as ThreadPool
# A person can climb one, two or three steps at a time
# Calculate the number of paths that the person can take to climb
# an 11 steps staircase
dict_results = {}

def numberOfPaths(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        # 1 1
        # 2
        return 2
    elif n == 3:
        # 1 1 1
        # 2 1
        # 1 2
        # 3
        return 4    
    # Calculate the paths comming from steps n-1, n-2 and n-3
    return  numberOfPaths(n-1) + numberOfPaths(n-2) + numberOfPaths(n-3)

# Simplified
def numberOfPaths2(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif dict_results.get(n) != None:
        return dict_results[n]
    result = numberOfPaths(n-1) + numberOfPaths(n-2) + numberOfPaths(n-3)
    dict_results[n] = result
    return  result
    
# Fooling arround with threads... need to overcome concurrency
def encapsulation(i):
    time_in = timer()
    calc = numberOfPaths2(i)
    time_out = timer()
    time_diff = timedelta(seconds=time_out - time_in)
    print('Took {0} seconds to run n = {1}. Result = {2}'.format(time_diff, i, calc))

pool = ThreadPool(16)

pool.map(encapsulation, range(1,50))
# for i in range(1,100):
#     t = threading.Thread(target=encapsulation, args = [i])
#     t.daemon = True
#     t.start()


    


