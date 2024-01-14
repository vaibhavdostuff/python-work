a = [1, 2, 3, 4, 5]
for x in range(len(a)):
    print (a[x])   

import random

# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 20)

# Ask the user to guess the number
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break
