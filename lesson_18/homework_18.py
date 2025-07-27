"""
Генератори:
task_01
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""

def even_numb_generator(N):
        for num in range(0, N + 1):
            if num % 2 == 0:
                yield num
N = 10
for even in even_numb_generator(N):
    print(even)

"""
task_02
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""

def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

N = 100
for num in fibonacci_generator(N):
    print(num)

"""
Ітератори:
task_03
Реалізуйте ітератор для зворотного виведення елементів списку.
# """

class  ReversedIterator:
    def __init__(self, num_list):
        self.num_list = num_list
        self.current = len(num_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.num_list[self.current]

my_iterator = [1,2,3,4,5]
reverse_iterator = ReversedIterator(my_iterator)
for item in reverse_iterator:
    print(item)

"""
task_04
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""

class  EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

for num in EvenIterator(10):
    print(num)

"""
Декоратори:
task_05
Напишіть декоратор, який логує аргументи та результати викликаної функції.
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling: {func.__name__}")
        logging.info(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)

"""
task_06
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""
def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Помилка] У функції '{func.__name__}' виникла помилка: {e}")
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))