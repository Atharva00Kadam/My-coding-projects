import random

user_input = input("Welcome to black jack! You will be given 2 cards,"
                         " and will have the choice whether to risk it or stand by it."
                         " Type 'yes' to play!: ")


arrayofnums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a1 = random.choice(arrayofnums)
a2 = random.choice(arrayofnums) # reveal dealer
b1 = random.choice(arrayofnums)
b2 = random.choice(arrayofnums)
b3 = random.choice(arrayofnums) #reveal 3rd user card

if user_input == "yes":
    print("Let's start! Your 2 cards are is: ")
    print(b1, b2)
    a = input("risk it or stand?: ")

    if a == "risk":
        print(b3)
        if b1 + b2 + b3 > 21 or a1 + a2 > b1 + b2 + b3:
            print("You lose!")
        else:
            print("You win!")
    if a == "stand":
        print("Below was the dealer's card")
        print(a2)
        if a1 + a2 > b1 + b2 + b3:
            print("You lose!")

        else:
            print("You win!")

print("The dealer's cards were:")
print(a1, a2)

