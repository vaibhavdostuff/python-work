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
def find_dup_char(input):
	x = filter(lambda x: input.count(x) >= 2, input)
	print(' '.join(set(x)))


# Driver Code
if __name__ == "__main__":
	input = 'vaibhavishere'
	find_dup_char(input)

#25
def find_duplicate_chars(string):
	# Create empty sets to store unique and duplicate characters
	unique_chars = set()
	duplicate_chars = set()

	# Iterate through each character in the string
	for char in string:
		# If the character is already in unique_chars, it is a duplicate
		if char in unique_chars:
			duplicate_chars.add(char)
		# Otherwise, add it to unique_chars
		else:
			unique_chars.add(char)
	return duplicate_chars

# Example usage:
print(find_duplicate_chars("vaibhavishere")) # Output: ['e', 'g', 'k', 's']

#26
from functools import reduce

def find_dup_char(input):
	x = reduce(lambda x, b: x + b if input.rindex(b) != input.index(b) and b not in x else x, input, '')
	print(x)


# Driver Code
if __name__ == "__main__":
	input = 'vaibhavishere'
	find_dup_char(input)

#27
def checkEmpty(input, pattern):
	
	# If both are empty
	if len(input)== 0 and len(pattern)== 0:
		return 'true'

	# If only pattern is empty
	if len(pattern)== 0:
		return 'false'

	while (len(input) != 0):

		# find sub-string in main string
		index = input.find(pattern)

		# check if sub-string founded or not
		if (index ==(-1)):
			return 'false'

		# slice input string in two parts and concatenate
		input = input[0:index] + input[index + len(pattern):]		 
	return 'true'

# Driver program
if __name__ == "__main__":
	input ='vaibhavishere'
	pattern ='vaibhav'
	print (checkEmpty(input, pattern))

#28
# Function to rotate string left and right by d length

def rotate(input,d):

	# slice string in two parts for left and right
	Lfirst = input[0 : d]
	Lsecond = input[d :]
	Rfirst = input[0 : len(input)-d]
	Rsecond = input[len(input)-d : ]

	# now concatenate two parts together
	print ("Left Rotation : ", (Lsecond + Lfirst) )
	print ("Right Rotation : ", (Rsecond + Rfirst))

# Driver program
if __name__ == "__main__":
	input = 'vaibhavishere'
	d=2
	rotate(input,d)

#29
from collections import deque

def rotate_string(s, d):
	deq = deque(s)
	if d > 0:
		deq.rotate(-d)
	else:
		deq.rotate(abs(d))
	return ''.join(deq)

s = 'vaibhavishere'
d = 2

left_rotated = rotate_string(s, d)
right_rotated = rotate_string(s, -d)

print("Left Rotation: ", left_rotated)
print("Right Rotation: ", right_rotated)

#30
code = '"hello" + "world"'
result = eval(code)
print(result) # Output: "hello world"

code = '["a", "b", "c"][1]'
result = eval(code)
print(result) # Output: "b"

#31
import types

code_string = "a = 6+5"
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.a) # 11

#32
# Python code to find the URL from an input string
# Using the regular expression
import re


def Find(string):

	# findall() has been used
	# with valid conditions for urls in string
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex, string)
	return [x[0] for x in url]


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))

#33
# Python code to find the URL from an input string

def Find(string):
	x=string.split()
	res=[]
	for i in x:
		if i.startswith("https:") or i.startswith("http:"):
			res.append(i)
	return res
			
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))

#34
# Python code to find the URL from an input string

def Find(string):
	x=string.split()
	res=[]
	for i in x:
		if i.find("https:")==0 or i.find("http:")==0:
			res.append(i)
	return res
			
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))

#35
from urllib.parse import urlparse

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'

# Split the string into words
words = string.split()

# Extract URLs from the words using urlparse()
urls = []
for word in words:
	parsed = urlparse(word)
	if parsed.scheme and parsed.netloc:
		urls.append(word)

# Print the extracted URLs
print("URLs:", urls)

#36
# Function to find permutations of a given string
from itertools import permutations

def allPermutations(str):
	
	# Get all permutations of string 'ABC'
	permList = permutations(str)

	# print all permutations
	for perm in list(permList):
		print (''.join(perm))
	
# Driver program
if __name__ == "__main__":
	str = 'ABC'
	allPermutations(str)

#37
from itertools import permutations
import string

s = "GEEK"
a = string.ascii_letters
p = permutations(s)

# Create a dictionary
d = []
for i in list(p):

	# Print only if not in dictionary
	if (i not in d):
		d.append(i)
		print(''.join(i))

#38

