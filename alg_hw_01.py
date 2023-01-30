from math import sqrt
import time

# сложность алгоритма O(1). Чтобы вывести все числа в ряд, то тогда сложность O(n).

def fib(n: int) -> int:
    sqrt_5 = sqrt(5)
    return ((((1 + sqrt_5) / 2)**n) - (((1 - sqrt_5) / 2)**n)) / sqrt_5

# сложность алгоритма O(n).

def fib2(n: int) -> int:
    list_fib = [0, 1]
    for i in range(2,n+1):
        list_fib.append(list_fib[i-1] + list_fib[i-2])
    return list_fib

# сложность алгоритма O(2^n). При вызове рукурсии для n = 40 считает уже достаточно долго. На малентких значениях счимтает быстрее.
def fib3(n: int) -> int:
    if n in (1,2):
        return 1
    else: return fib3(n - 1) + fib3(n - 2)

# ------------------------------------------------------------------------------------
n: int = 10

start1 = time.time() 
# print(*[fib(i) for i in range(1, n + 1)])  # print numbers only
# print([fib(i) for i in range(1,n + 1)]) # print in list format
fib(n)
span1: float = time.time() - start1
print(f'fib O(1):   {"{:.10f}".format(span1)}')

start2 = time.time() 
# lister = fib2(n)
# print(*lister[1:])
fib2(n)[n]
span2: float = time.time() - start2
print(f'fib O(n):   {"{:.10f}".format(span2)}')

start3 = time.time() 
# print(*[fib3(i) for i in range(1, n + 1)])  # print numbers only
fib3(n)
span3: float = time.time() - start3
print(f'fib O(2^n): {"{:.10f}".format(span3)}')
