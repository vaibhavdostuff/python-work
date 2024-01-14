a = [1, 2, 3, 4, 5]
for x in range(len(a)):
    print (a[x])   

#1
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

#2
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

story = f"The {adjective} {noun} likes to {verb} in the park."
print(story)

#3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"The result is: {result}")

#4
import random

while True:
    input("Press Enter to roll the dice...")
    dice_result = random.randint(1, 6)
    print(f"The dice rolled a {dice_result}")
    play_again = input("Roll again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

#5
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"There are {word_count} words in the sentence.")

#6
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)
print(f"The computer chose: {computer_choice}")
print(determine_winner(user_choice, computer_choice))

