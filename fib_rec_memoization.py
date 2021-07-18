fib_dict = {1:1, 2:1}

def fib_rec_mem(n):
    # Known values of fib series
    if n <= 2:
        return 1
    else:
        # IF we have not calculated the value 'n'; calculate it
        if fib_dict.get(n) == None:
            calculate = fib_rec_mem(n-1) + fib_rec_mem(n-2)
            fib_dict[n] = calculate
            return calculate
        # ... return the value at n if we know it
        else:
            return fib_dict[n]

print(fib_rec_mem(15))
print(fib_dict.values())

# [1,2,3,4].insert()