# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

text = input("Enter text with 'h': ")
while not 'h' in text.lower():
    text = input("Please try again.Enter text with 'h': ")
print("Accepted!")