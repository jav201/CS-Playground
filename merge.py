import numpy as np

# Array size
size = 80

# 2 arrays already sorted from max to min (min is popped)
array_1 = sorted(np.random.randint(99, size=size), reverse=True)
array_2 = sorted(np.random.randint(99, size=size), reverse=True)

def merge(array_1, array_2):
    out_list = []
    while len(array_1) > 0 and len(array_2) > 0:
        if array_1[-1] < array_2[-1]:
            out_list.append(array_1.pop())
        else:
            out_list.append(array_2.pop())
    if len(array_1) == 0:
        out_list = out_list + array_2
    else:
        out_list = out_list + array_1
    return out_list
    
print(merge(array_1, array_2))


