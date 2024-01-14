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

#7
import random

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

word_to_guess = choose_word()
guessed_letters = []
attempts = 6

while attempts > 0:
    print(display_word(word_to_guess, guessed_letters))
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    if guess not in word_to_guess:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts remaining.")
        if attempts == 0:
            print("You ran out of attempts. Game over!")
    else:
        print("Correct!")

    if "_" not in display_word(word_to_guess, guessed_letters):
        print(f"Congratulations! You guessed the word: {word_to_guess}")
        break

#8
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest...")
    choice = input("Do you go left or right? ").lower()
    if choice == "left":
        print("You encounter a bear! Game over.")
    elif choice == "right":
        print("You find a treasure chest! You win!")
    else:
        print("Invalid choice. Try again.")
        start_game()

start_game()
