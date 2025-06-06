"""
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
"""
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where —— " said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '" —— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print(alice_in_wonderland.count("'"))
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
square = black_sea + azov_sea
print("The square is", square, "km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
orders_total = 375291
warehouse_3 = orders_total - 222950
warehouse_1 = orders_total - 250449
warehouse_2 = orders_total - (warehouse_1 + warehouse_3)
print(f'''Warehouse 1 has {warehouse_1} orders
Warehouse 2 has {warehouse_2} orders
Warehouse 3 has {warehouse_3} orders''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
period = 18
month_payment = 1179
order_total = period * month_payment
print("Total order price is", order_total, "UAH.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(8019 % 8)
print(9907 % 9)
print(2789 % 5)
print(7248 % 6)
print(7128 % 5)
print(19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza = 274
medium_pizza = 218
Juice = 35
cake = 350
water = 21
total_order_amount = (
        (large_pizza * 4) + (medium_pizza * 2)
        + (Juice * 4) + cake + (water * 3)
)
print("Total order amount =", total_order_amount, "UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_on_page = 8
pages = all_photos // photos_on_page
print("Ihor needs", pages, "pages.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
petrol_per_100km = 9
tank_size = 48
needed_petrol = (distance * petrol_per_100km)/100
needed_petrol_stop = needed_petrol // tank_size
print(needed_petrol)
print(int(needed_petrol_stop))