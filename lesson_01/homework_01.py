# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4 * apples
print(banana)

# task 05 == виправте назви змінних
side1 = 1
side2 = 2
side3 = 3
side4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side1 + side2 + side3 + side4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
all_trees = apple_trees + pear_trees + plum_trees
print ("Всього посадили", all_trees, "дерев.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature = 0
morning_tempr = temperature + 5
day_tempr = morning_tempr - 10
evening_tempr = day_tempr + 4
print ("Температура надвечір:", evening_tempr, "°C")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
total_today = (int((boys - 1) + (girls - 2)))
print("Сьогодні", total_today, "дитини у театральному гуртку.")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1 = 8
book2 = book1 + 2
book3 = (book1 + book2) / 2
total_price = book1 + book2 + book3
print("Загальна вартість книг = ", total_price, "грн.")
