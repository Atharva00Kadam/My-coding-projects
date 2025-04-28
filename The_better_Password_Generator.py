import random
letters = ["a", "b", "c", "d", "A", "B", "C", "D"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "@", "#", "$", "%", "&", "$#]}"]

print("Welcome to my Python Password Generator! :)")
nr_letters = int(input("How many letters do ya want? \n"))
nr_numbers = int(input("How many numbers do ya want? \n"))
nr_special_characters = int(input("How many special characters do ya need? \n"))

password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_special_characters + 1):
    password += random.choice(special_characters)

print(password)
