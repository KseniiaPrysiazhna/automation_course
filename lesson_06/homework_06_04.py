# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

number = [x for x in range(10)]
total = sum(x for x in number if x % 2 == 0)
print(f"Sum of all even numbers = {total}")