import numpy as np

arr_1 = list(np.random.randint(10000, size=10000))
# Sort from MIN to MAX
def quick_sort(array_1):
    # BASE CASE 1 - Array too short
    arr_length = len(array_1)
    if arr_length < 2:
        return array_1
    # BASE CASE 2 - Array is len 2
    elif arr_length == 2:
        if array_1[0] < array_1[1]:
            return array_1
        else:
            return array_1[::-1]
    # Recuirsive case
    else:
        pivot = array_1.pop()
        arr_left = [x for x in array_1 if x <= pivot]
        arr_rigth = [x for x in array_1 if x > pivot]
        return quick_sort(arr_left) + [pivot] + quick_sort(arr_rigth)

print(arr_1)
print(quick_sort(arr_1))