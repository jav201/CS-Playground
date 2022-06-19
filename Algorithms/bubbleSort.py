listSort = list(map(int, list('18237829405947273940')))

def bubbleSort(arr):
    swap = None
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            swap = True
    if swap is not None:
        return bubbleSort(arr)
    return arr
        
print(bubbleSort(listSort))