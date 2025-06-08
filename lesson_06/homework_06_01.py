text = input("Enter text: ")
unique_chars = set(text)
if len(unique_chars) > 10:
    print("True")
else:
    print("False")