import random

Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
Lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Special = ['!', '@', '#', '$', '%', '^', '*']

# Pick one random item from each list
alo = random.choice(Uppercase)
blo = random.choice(Lowercase)
clo = random.choice(Numbers)  # No need to index into the list here
dlo = random.choice(Special)

# Construct the final password correctly
print("1234" + alo + blo + str(clo) + dlo)
