# task 10
"""ДЗ 06.01: Функція яка рахує сумму усіх ПАРНИХ чисел в лісті"""

def sum_even_numbers(number):
    total = sum(x for x in number if x % 2 == 0)
    print(f"Sum of all even numbers = {total}")