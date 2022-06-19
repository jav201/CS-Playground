listSort = list(map(int, list('18237829405947273940')))

def insertsort(arr):
    def insertElement(l, array):
        for i in range(len(array)):
            if array[i] > l:
                pass
            else:
                array = array[:i] + [l] + array[i:]
                return array
        return array

    sortedArray = arr[:1]
    unsortedArray = arr[1:]
    element = unsortedArray.pop(0)
    while unsortedArray:
        sortedArray = insertElement(element, sortedArray)
        element = unsortedArray.pop(0)
    return sortedArray

print(insertsort(listSort))
