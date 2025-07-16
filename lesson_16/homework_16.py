"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""

class Rhomb:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("The side_a must be more than 0.")
            super().__setattr__(name, value)

        elif name == "corner_a":
            if not (0 < value < 180):
                raise ValueError("The corner_a must be between 0 and 180.")
            super().__setattr__("corner_a", value)
            super().__setattr__("corner_b", 180 - value)
            return

        else:
            super().__setattr__(name, value)

rhomb = Rhomb(side_a = 15, corner_a = 70)
print(f"Сторона a: {rhomb.side_a}")
print(f"Кут a: {rhomb.corner_a}")
print(f"Кут b: {rhomb.corner_b}")