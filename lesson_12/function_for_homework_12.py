# function 01
"""Функція, яка обчислює суму двох чисел.
"""
def sum_two_numbers (a, b):
    return a + b

# function 02
"""функція, яка розрахує середнє арифметичне списку чисел.
"""
def average (numbers):
    return sum(numbers) / len(numbers)

# function 03
"""функція, яка приймає рядок та повертає його у зворотному порядку
"""
def reverse_string(text):
    return text[::-1]

# function 04
"""функція яка викликає цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""

def find_h_in_text():
    text = input("Enter text with 'h': ")
    while not 'h' in text.lower():
        text = input("Please try again.Enter text with 'h': ")
    return "Accepted!"

# function 05
"""Функція яка допомогає порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - виводить в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

def uniq_symbols_more_than_10():
    text = input("Enter text: ")
    return len(set(text)) > 10