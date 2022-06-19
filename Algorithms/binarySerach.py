import numpy as np

def binarySearch(array, lookfor):
    global counter
    arrLength = len(array)
    # Case 1 - Array is of len > 1
    midPoint = arrLength // 2
    numMidPoint = array[midPoint]
    if arrLength > 1 and numMidPoint > lookfor:
        counter += 1
        return binarySearch(array[:midPoint], lookfor)
    elif arrLength > 1:
        counter += 1
        return binarySearch(array[midPoint:], lookfor)
    # Base case - Array is of len 1 
    elif arrLength == 1 and array[0] == lookfor:
        return f'Found {lookfor} in {counter} counts'
    # You need the recursive result
    return f'{lookfor} Not Found'


for i in range(222222):
    npArray = np.random.randint(0,1000,500)
    # npArray = np.insert(npArray, 1, 443)
    sortedList = sorted(npArray)
    lookfor = 443
    counter = 0
    print(binarySearch(sortedList, lookfor))