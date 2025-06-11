# task 1
"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers (a, b):
    return a + b
print(sum_two_numbers(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average (numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(words):
    longest_word = max(words, key=len)
    return longest_word
print(longest_word_in_list(["test", "testtest"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 - 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""ДЗ 06.02: функція яка викликає цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""

def find_h_in_text():
    text = input("Enter text with 'h': ")
    while not 'h' in text.lower():
        text = input("Please try again.Enter text with 'h': ")
    print("Accepted!")

find_h_in_text()

# task 8
"""ДЗ 06.03: Функція яка формує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими"""

def find_str_only(lst1):
    lst2 = [item for item in lst1 if isinstance(item, str)]
    print(lst2)

find_str_only(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])

# task 9
"""ДЗ 06.01: Функція яка допомогає порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - виводить в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

def uniq_symbols_more_than_10():
    text = input("Enter text: ")
    print ((len(set(text)) > 10))

uniq_symbols_more_than_10()

# task 10
"""ДЗ 06.01: Функція яка рахує сумму усіх ПАРНИХ чисел в лісті"""

def sum_even_numbers(number):
    total = sum(x for x in number if x % 2 == 0)
    print(f"Sum of all even numbers = {total}")

sum_even_numbers([x for x in range(10)])