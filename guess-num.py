import random

def Ez_level(a):
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts:
        k = int(input(f"Attempt {attempts+1}/{max_attempts}. Enter your guess: "))
        if k == a:
            print("You have won! "
                  "\n Print the number of the range ")
            return
        else:
            s = k
            if s - 10 < s < s + 10:
                print("Very close!")
            elif s - 20 < s < s + 20:
                print("Close..")
            else:
                print("Far away...")
        attempts += 1
    print(f"Sorry, you're out of attempts. The number was {a}.")

# Game setup
a = random.randint(1, 100)
print("Welcome to the number guessing game! Guess the right number and the victory will be yours.")
difficulty = input("Which difficulty you want to play with? Ez/Hard: ").strip().lower()

if difficulty == 'ez':
    Ez_level(a)
elif difficulty == 'hard':
    print("Hard mode isn't implemented yet.")
else:
    print("Invalid difficulty selected.")
