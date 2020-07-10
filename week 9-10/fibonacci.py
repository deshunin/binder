# fibonacci numbers and memoization

# standart regursion form (for n = 34 it takes 1.6 sec)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

# fastest so far mine form using list operations (for n = 34 it takes 43 microsec)
def fib(n):
    fib_lst = [0,1]
    for k in range(2, n+1):
        f = fib_lst[k-2] + fib_lst[k-1]
        fib_lst.append(f)
    return fib_lst[n]

# a litle slower then previous form using numpy operations (for n = 34 it takes 106 microsec)
import numpy as np
def fibon(n):
    fibon_arr = np.zeros(n+1, int)
    fibon_arr[0] = 0
    fibon_arr[1] = 1
    for k in range(2, n+1):
        fibon_arr[k] = fibon_arr[k-2] + fibon_arr[k-1]
    return fibon_arr[n]

# the slowest way from MIT open course 6.006 Lecture 19 to demonstrate memoization technique
# in spite of the instructor's claim it takes 2.5 times slower that the first standart recursion
# (for n = 34 it takes 4 sec)
memo = []
def fib_memo(n):
    if len(memo) == n + 1:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib_memo(n-2) + fib_memo(n-1)
    memo.append(f)
    return f

# the fast way to calculate fibonacci number using dictionary and memoization technique
# (for n = 34 it takes  30 microsec). coorect implementation of the algorithm from 6.006 Lecture 19

fib_dict = {}
def fibb(n):
    if n in fib_dict:
        return fib_dict[n]
    if n <= 2:
        f = 1
    else:
        f = fibb(n-2) + fibb(n-1)
    fib_dict[n] = f
    return f
