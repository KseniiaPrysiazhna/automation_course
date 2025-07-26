"""20 імпортів
Імпорт ваших функцій, вбудованих, інстальованих
(вже інстальовані знайдете в папці vevn -> libs)
Застосовути всі види імпорту
from ... import...
import ....
from ... import *
from ... import ... as .... """

#1
from datetime import datetime
now = datetime.now()
print(now)

#2
from operator import add
result = add(2, 3)
print(result)

#3
from statistics import mean

data = [10, 20, 30, 40]
print("Середнє значення:", mean(data))


#4
import pytest
def test_example():
    a = 1
    b = 8
    if a + b != 9:
        pytest.fail("Помилка: Сума a та b не дорівнює 9")

#5
import math
result = math.sqrt(100)
print(result)

#6
from math import *
print("Корінь з 144:", sqrt(144))

#7
import random
random_number = random.randint(0, 100)
print(random_number)

#8
from datetime import *
today = date.today()
print("Сьогоднішня дата:", today)

#9
from statistics import mean as avg
print(avg([1, 2, 3, 4]))

#10
from file_17_02 import sum_even_numbers

sum_even_numbers([1, 2, 3, 4, 5, 6])

#11
import json
res = json.dumps([6, 9, 3])
print(dir())

#12
from collections import Counter

letters = Counter("banana")
print("Літери та їх кількість:", letters)

#13
from file_17 import multiplication_table

multiplication_table(2)

#14
from file_17_03 import sum_two_numbers as sum
result = sum(5, 6)
print(result)

#15
import os
current_directory = os.getcwd()
print(current_directory)

#16
import sys
print(sys.version)

#17
import re
pattern = re.compile(r'\\b\\w+\\b')   # задаємо регуляний вираз
text = "Hello, world!"
matches = pattern.findall(text)    # здійснюємо пошук у тексті за виразом
print(matches)

#18
from file_17_04 import reverse_string

print(reverse_string("python"))

#19
import numpy as np
print(np.array([1, 2, 3]))

#20
from unittest.mock import patch
with patch('builtins.input', return_value='yes'):
    answer = input("Are you sure?")
    print("Answer:", answer)