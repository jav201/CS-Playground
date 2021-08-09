import numpy as np

# Array size
a_size = 10
# Generate a random array
array_out = np.random.randint(99, size=a_size)
print(array_out)

for i in range(a_size):
    # Iterate through all the list
    current = array_out[i]
    idx2swap = i
    # Iterate through a sublist excluding position < i
    for j, num in enumerate(array_out[i::], i):
        if num < current:
            idx2swap = j
            current = num
    # Swap smallest number at i position
    array_out[idx2swap] = array_out[i]      
    array_out[i] = current

print(array_out)