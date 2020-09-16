fib_dict = {1:1, 2:1}

def fib_rec_mem(n):
    if n <= 2:
        return 1
    else:
        if n not in fib_dict.keys():
            calculate = fib_rec_mem(n-1) + fib_rec_mem(n-2)
            fib_dict[n] = calculate
            return calculate
        else:
            return fib_dict[n]

print(fib_rec_mem(10))
print(fib_dict.values())