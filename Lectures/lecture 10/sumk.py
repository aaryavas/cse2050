import timeit


def sumk(k): #O(k)
    temp_sum = 0
    
    for i in range(1, k+1):
        temp_sum += 1
    
    return temp_sum


#sum(k) = k + (k-1) + (k-2) + ... + 1
#sum(k)  = K  +sum(k-1)
#                k-1 + sum(k-2)
#                    k-2 +sum(k-3)

def sumk_recr(k):
    
    if k ==1:
        return 1
    
    return k + sumk_recr(k-1) #my function calls itself!


#wrtie a recursive factorial function
#factorial(n)  = n * (n-1)

def factorialrec(n):
    #base case
    if n in {0,1}:
        return 1
    
    
    return n * factorialrec(n-1)

assert factorialrec(0) == 1
assert factorialrec(1) == 1

#find the kth fibonacci number
#fibs -  1,1,2,3,5,8,13
#each number is the sum of the 2 previous numbers 
#base cases:
#      fib(1) =1
#      fib(2) = 1


def fib(k):
    #base cases
    if k in {1,2}: 
        return 1
    
    return fib(k-1) + fib(k-2)
def fib_memo(n, solved,: dict):
    if solved is None:
        solved = {1:1, 2:1}
    
    if n in {1,2} : return 1
     
    if n in solved:return solved[n]
     
    solved[n] = fib(n-1, solved) + fib(n-2, solved)
     
    return solved

for n in [10, 20, 30, 40, 50]:
        run_str = f"fib({n})"
        print(f"n = {n}\t{timeit.timeit(run_str, number=1, globals=globals()):.3g} s")        
    
    
    
x = sumk_recr(10)

assert sumk_recr(0) == 0
assert sumk_recr(1) == 1
assert sumk_recr(10) == 10


for func in [sumk, sumk_recr]:
        t = timeit.timeit(f'{func.name}(20)', globals=globals())
        print(f"{func.name}: {t:.3g} s")