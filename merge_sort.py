import numpy as np

def merge(array_1, array_2):
    out_list = []
    while len(array_1) > 0 and len(array_2) > 0:
        if array_1[-1] > array_2[-1]:
            out_list.append(array_1.pop())
        else:
            out_list.append(array_2.pop())
    if len(array_1) == 0:
        out_list = out_list + array_2
    else:
        out_list = out_list + array_1
    return out_list


def merge_sort(array_3):
    if len(array_3) == 1:
        return array_3
    else:
        half_point = len(array_3)//2
        left_l  = array_3[:half_point:]
        right_l = array_3[half_point::]
        return merge(merge_sort(left_l), merge_sort(right_l))

arr = list(np.random.randint(10, size=10))
print(arr)
print(merge_sort(arr))
