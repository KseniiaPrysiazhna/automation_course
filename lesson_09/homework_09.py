# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючий студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade

    def greet(self):
        return f"My full name is {self.name} {self.surname}."

    def change_grade(self, new_grade):
        self.grade = new_grade
        return f"My new grade is {new_grade}"


student = Student("Kseniia", "Prysiazhna", 28, 90)

print(student.greet())
print(student.grade)
print(student.change_grade(100))
print(student.grade)