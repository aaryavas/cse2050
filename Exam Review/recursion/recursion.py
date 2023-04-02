def f(k):
    if k > 0:
        return f(k-1) + k
    return 0
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))