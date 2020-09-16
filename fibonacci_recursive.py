def fibo_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

for _ in range(1, 10):
    print(fibo_recursive(_))
# print(fibo_recursive(10))