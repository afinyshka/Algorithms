def sieve_eratosthenes (n: int) -> list:
    """Функция выводит список true или false последовательно для чисел от нуля до заданного числа n,
        не включая его, является ли число простым"""
    listt = [True] * n
    listt[0] = listt[1] = False
    for k in range (2, n):
        if listt[k]:
            for j in range(2 * k, n, k):
                listt[j] = False
    return listt

def is_prime_numbers_printer(n: int) -> str:
    """Печатает список чисел от 2 до n включительно с обозначением является ли оно простым (e.g. 2 - prime number)"""
    listt = sieve_eratosthenes(n + 1)
    for i in range (2, len(listt)):
        print(f"{i} - {'prime number' if listt[i] else 'not'}")

prime_numbers_list = is_prime_numbers_printer(10)
prime_numbers_list = is_prime_numbers_printer(11)
prime_numbers_list = is_prime_numbers_printer(22)
prime_numbers_list = is_prime_numbers_printer(33)
# n = 10

# listt = sieve_of_eratosthenes(n+1)
# print(listt)
# for i in range (2, n+1):
#     print(f'{i} - {"prime number" if listt[i] else "not"}')

