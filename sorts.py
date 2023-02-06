from functools import reduce


def insert_sort(listt: list) -> None:
    """Сортировка элементов массива методом вставки"""
    l = len(listt)
    for i in range(1, l):
        for j in range(i, 0, -1):
            if listt[j] < listt[j - 1]:
                listt[j], listt[j - 1] = listt[j - 1], listt[j]


def choise_sort(listt: list) -> None:
    """Сортировка элементов массива методом выбора"""
    # 3 4 5 9 1 ->
    l = len(listt)
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            if listt[i] > listt[j]:
                listt[i], listt[j] = listt[j], listt[i]


def bubble_sort(listt: list) -> None:
    """Сортировка элементов массива методом пузырька"""
    l = len(listt)
    for i in range(1, l):
        for j in range(0, l - i):
            if listt[j] > listt[j + 1]:
                listt[j + 1], listt[j] = listt[j], listt[j + 1]


# Поразрядная сортировка: Radix sort

# get number of digits in largest item
def num_digits(arr):
    """Возвращает длину наибольшего элемента массива"""
    maxDigit = 0
    for num in arr:
        maxDigit = max(maxDigit, num)
    return len(str(maxDigit))
 
# flatten into a 1D List
def flatten(arr):
    """Возвращает сумму элементов массива"""
    return reduce(lambda x, y: x + y, arr)
 
def radix_sort(arr):
    """Сортировка элементов массива методом поразрядной сортировки"""
    digits = num_digits(arr)
    for digit in range(0, digits):
        temp = [[] for i in range(10)]
        for item in arr:
            num = (item // (10 ** digit)) % 10
            temp[num].append(item)
        arr = flatten(temp)
    return arr


# Сортировка подсчетом Count sort
def count_sort(listt: list) -> list:
    """Сортировка элементов массива методом подсчета"""
    listt_cnt = [0] * (max(listt) + 1)
    for i in range(len(listt)):
        listt_cnt[listt[i]] += 1
    print(listt_cnt)
    list_sorted = []
    for k in range(len(listt_cnt)):
        for j in range(listt_cnt[k]):
            list_sorted.append(k)
            # print(k, sep=", ", end=" ")
    return  list_sorted

def sorting_by_counting() -> None:
    """Сортировка элементов массива методом подсчета при вводе с клавиатуры"""
    a = list(map(int, input().split()))  # считывание списка
    # генерация списка нулей длиной в максимальный элемент списка a
    cnt = [0] * (max(a) + 1)
    for item in a:
        cnt[item] += 1   # когда мы встречаем число в списке, увеличиваем его значение на 1
    # добавляем count раз число num в результат
    result = [num for num, count in enumerate(cnt) for i in range(count)]
    print(result)  # выводим отсортированный список

def sorting_by_counting(listt: list) -> list:
    """Сортировка элементов массива методом подсчета"""
    cnt = [0] * (max(listt) + 1)
    for i in listt:
        cnt[i] += 1
    lst = []
    print(cnt)
    for k, count in (enumerate(cnt)):
        for i in range(count):
            lst.append(k)
    return lst


def test_sort_algorithms(sort_algorithm: callable) -> None:
    """Проверка методов сортировки"""
    print("Тестируем: ", sort_algorithm.__doc__)
    print("Testcase #1: ", end="")
    list_A = [2, 4, 3, 7, 1]
    list_B = [1, 2, 3, 4, 7]
    sort_algorithm(list_A)
    print("Ok" if list_A == list_B else "Fail")

    print("Testcase #2: ", end="")
    list_A = list(range(10, 0, -1)) + list(range(20, 10, -1))
    list_B = list(range(1, 21))
    sort_algorithm(list_A)
    print("Ok" if list_A == list_B else "Fail")

    print("Testcase #3: ", end="")
    list_A = [2, 4, 4, 2, 1]
    list_B = [1, 2, 2, 4, 4]
    sort_algorithm(list_A)
    print("Ok" if list_A == list_B else "Fail")

    print("Testcase #4: ", end="")
    list_A = [5, 9, 6, 9, 0, 5, 3, 2, 7, 6, 7, 6]
    list_B = [0, 2, 3, 5, 5, 6, 6, 6, 7, 7, 9, 9]
    sort_algorithm(list_A)
    print("Ok" if list_A == list_B else "Fail")

[5, 9, 6, 9, 0, 5, 3, 2, 7, 6, 7, 6]

if __name__ == "__main__":
    test_sort_algorithms(insert_sort)
    test_sort_algorithms(choise_sort)
    test_sort_algorithms(bubble_sort)


    ls = [5, 9, 6, 9, 0, 5, 3, 2, 7, 6, 7, 6]
    # count_sort(ls)
    print(sorting_by_counting(ls))
    # print(count_sort(ls))
    # print(list(enumerate(ls)))

    # elements = ('foo', 'bar', 'baz')
    # for count, elem in enumerate(elements):
    #     print(count, elem)

    lk = flatten([1, 2, 3, 4, 5])
    print(lk)