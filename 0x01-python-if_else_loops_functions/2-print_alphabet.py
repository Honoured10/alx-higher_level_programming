# This program prints alphabets in lowercase without a new line
alphabet = range(97, 123)
for letter in alphabet:
    print(f"{chr(letter)}", end='')
