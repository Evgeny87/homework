"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    def filter_even_num(in_num):
        if (in_num % 2) == 0:
            return True
        else:
            return False

    def filter_odd_num(in_num):
        if (in_num % 2) != 0:
            return True
        else:
            return False

    # кусок кода от сюда https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python
    def filter_is_prime_num(in_num):
        if in_num > 1:
            if in_num % 2 == 0:
                return in_num == 2
            d = 3
            while d * d <= in_num and in_num % d != 0:
                d += 2
            return d * d > in_num

    if filter_type == ODD:
        return list(filter(filter_odd_num, numbers))
    elif filter_type == EVEN:
        return list(filter(filter_even_num, numbers))
    elif filter_type == PRIME:
        return list(filter(filter_is_prime_num, numbers))