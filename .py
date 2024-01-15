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

#9
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature)}°F")
elif unit == "F":
    print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature)}°C")
else:
    print("Invalid unit.")

#10
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#11
def pig_latin(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in 'aeiou':
            pig_latin_words.append(word + 'way')
        else:
            pig_latin_words.append(word[1:] + word[0] + 'ay')
    return ' '.join(pig_latin_words)

input_text = input("Enter text to translate to Pig Latin: ")
print("Pig Latin:", pig_latin(input_text.lower()))

#15
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter text to encrypt: ")
shift_amount = int(input("Enter shift amount: "))
encrypted_text = caesar_cipher(plaintext, shift_amount)
print(f"Encrypted text: {encrypted_text}")

#16
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password_length = int(input("Enter desired password length: "))
print("Generated password:", generate_password(password_length))

#17
todo_list = []

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task to add: ")
        todo_list.append(task)
    elif choice == "2":
        if todo_list:
            print("Tasks:")
            for i, task in enumerate(todo_list):
                print(f"{i + 1}. {task}")
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(todo_list):
                del todo_list[index]
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
    elif choice == "3":
        if todo_list:
            print("Tasks:")
            for i, task in enumerate(todo_list):
                print(f"{i + 1}. {task}")
        else:
            print("No tasks.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

#18
def count_word_frequency(text):
    words = text.split()
    word_frequency = {}
    for word in words:
        word = word.lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

input_text = input("Enter a text: ")
frequencies = count_word_frequency(input_text)
for word, frequency in frequencies.items():
    print(f"{word}: {frequency} times")

#19
import datetime
import time

alarm_time = input("Set the alarm time (HH:MM): ")
while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("ALARM!")
        break
    else:
        print(f"Current time is {current_time}. Waiting for {alarm_time}.")
        time.sleep(60)  # Check every minute
