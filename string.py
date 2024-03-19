#1
print("first string program python") 

#2 
String1 = '2 string program python'
print(String1) 

String1 = "vaibhav here"
print("\nfirst string program python") 
print(String1) 

String1 = '''vaibhav here'''
print("\nfirst string program python") 
print(String1) 

String1 = '''vaibhav
is
here'''
print("\nfirst string program python") 
print(String1) 

#3
String1 = "vaibhav is here"
print("starting String: ") 
print(String1) 

print("\nFirst character of String is: ") 
print(String1[0]) 

print("\nLast character of String is: ") 
print(String1[-1]) 

#4 
String1 = "vaibhav is here"
print(String1) 

print(String1[1:10]) 

print(String1[1:-2]) 

#5
String1= "vaibhav is here"
print(String1[::-1])

#6
String1= "vaibhav is here"

String1= "1".join(reversed(String1)) 
  
print(String1)

#7
String1 = "Hello,vaibhav is here"
print(String1) 

#1 
list1 = list(String1) 
list1[2] = '1'
String2 = ''.join(list1)
print(String2) 

#2 
String3 = String1[0:2] + '2' + String1[3:] 
print(String3) 

    
#8
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

#1 
list1 = list(String1) 
list1[2] = '1'
String2 = ''.join(list1) 
print(String2) 

#2 
String3 = String1[0:10] + '1' + String1[7:] 
print(String3)

#9
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 


String1 = "working on programm"
print("\nUpdated String: ") 
print(String1) 

#10
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

print("Deleting character at 2nd Index: ") 
#del String1[2] 
print(String1)

#11
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

String2 = String1[0:10] + String1[7:] 
print("\nDeleting character at 2nd Index: ") 
print(String2) 

#12
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 


del String1 
print("\nDeleting entire String: ") 
#print(String1) 

#13
String1 = '''Hello,vaibhav is here'''
print(String1) 


String1 = 'Hello,vaibhav is here'
print(String1) 


String1 = "Hello,vaibhav is here"
print(String1) 

String1 = "C:\\Python\\string\\"
print(String1)
  

String1 = "Hi\tstring"
print("\nTab: ") 
print(String1) 
  

String1 = "Python\nstring"
print("\nNew Line: ") 
print(String1) 

#14
# Printing hello in octal 
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1)

# Printing Geeks in HEX 
String1 = "This is \x76\x61\x69\x62\x68\x61\x76 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x76\x61\x69\x62\x68\x61\x76 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1)

#15
String1 = "{} {} {}".format('vaibhav', 'is', 'here')
print(String1) 

String1 = "{2} {0} {1}".format('vaibhav', 'is', 'here')
print(String1)


String1 = "{h} {i} {v}".format(v='vaibhav', i='is', h='here')
print(String1) 

#16
String1 = "{0:b}".format(10)
print(String1) 


String1 = "{0:e}".format(165.6458)
print(String1) 

String1 = "{0:.2f}".format(1/7)
print(String1)

#17
# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('vaibhav', 
                                          'is',  
                                          'here') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 
  
# To demonstrate aligning of spaces 
String1 = "\n{0:^16} was started in {1:<4}!".format("vaibhav is here", 
                                                    2023) 
print(String1) 

#18
# Python Program for 
# Old Style Formatting 
# of Integers 
  
Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' % Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' % Integer1) 

#19
import re


def replace_substring(test_str, s1, s2):
	# Replacing all occurrences of substring s1 with s2
	test_str = re.sub(s1, s2, test_str)
	return test_str


# test
test_str = "vaibhavishere"
s1 = "vaibhav"
s2 = "abcd"
print(replace_substring(test_str, s1, s2))

#20
def replace_substring(test_str, s1, s2):
	# Initialize an empty string to store the result
	result = ""
	# Initialize a variable to keep track of our position in the string
	i = 0
	# Loop through the string one character at a time
	while i < len(test_str):
		# Check if the current substring matches the substring we want to replace
		if test_str[i:i+len(s1)] == s1:
			# If it does, add the replacement substring to the result and move the pointer forward
			result += s2
			i += len(s1)
		else:
			# If it doesn't, add the current character to the result and move the pointer forward
			result += test_str[i]
			i += 1
	# Return the final result
	return result

# test
test_str = "vaibhavishere"
s1 = "vaibhav"
s2 = "abcd"
print(replace_substring(test_str, s1, s2))

#21
def duplicate_characters(string):
	# Create an empty dictionary
	chars = {}

	# Iterate through each character in the string
	for char in string:
		# If the character is not in the dictionary, add it
		if char not in chars:
			chars[char] = 1
		else:
			# If the character is already in the dictionary, increment the count
			chars[char] += 1

	# Create a list to store the duplicate characters
	duplicates = []

	# Iterate through the dictionary to find characters with count greater than 1
	for char, count in chars.items():
		if count > 1:
			duplicates.append(char)

	return duplicates

# Test cases
print(duplicate_characters("vaibhavishere"))

#22
from collections import Counter


def find_dup_char(input):

	# now create dictionary using counter method
	# which will have strings as key and their
	# frequencies as value
	WC = Counter(input)

	# Finding no. of occurrence of a character
	# and get the index of it.
	for letter, count in WC.items():
		if (count > 1):
			print(letter)


# Driver program
if __name__ == "__main__":
	input = 'vaibhavishere'
	find_dup_char(input)

#23
def find_dup_char(input):
	x = filter(lambda x: input.count(x) >= 2, input)
	print(' '.join(set(x)))


# Driver Code
if __name__ == "__main__":
	input = 'vaibhavishere'
	find_dup_char(input)

#24
