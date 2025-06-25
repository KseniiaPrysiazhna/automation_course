# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size


# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур,
# та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур,
# та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height + self.__width) * 2


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

class Triangle(Shape):
    def __init__(self, leg1, leg2, hypotenuse, height):
        self.__leg1 = leg1
        self.__leg2 = leg2
        self.__height = height
        self.__hypotenuse = hypotenuse

    def area(self):
        return (self.__hypotenuse * self.__height)/2

    def perimeter(self):
        return self.__leg1 + self.__leg2 + self.__hypotenuse


shapes = [
    Rectangle(4, 5),
    Square(3),
    Triangle(6, 4, 3, 4)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
    print(f"{shape.__class__.__name__} perimeter: {shape.perimeter():.2f}")