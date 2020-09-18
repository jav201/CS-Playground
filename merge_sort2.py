import numpy as np

arr1 = list(np.random.randint(100, size=100))

# Sort min to max
def merge(array_1, array_2):
    out_list = []
    while len(array_1) > 0 and len(array_2) > 0:
        if array_1[0] < array_2[0]:
            out_list.append(array_1[0])
            array_1 = array_1[1::]
        else:
            out_list.append(array_2[0])
            array_2 = array_2[1::]
    if len(array_1) == 0:
        out_list = out_list + array_2
    else:
        out_list = out_list + array_1
    return out_list


def split(arr_1):
    # BC Array of length 1; return array size 1
    if len(arr_1) == 1:
        return arr_1
    # Recursive - Split and call merge over resulting arrays 
    mp = len(arr_1) // 2
    arr1 = arr_1[:mp:]
    arr2 = arr_1[mp::]
    return merge(split(arr1), split(arr2))

print(arr1)
print(split(arr1))