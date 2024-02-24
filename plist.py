#1
list1 = [2, 7, 5, 64, 14]
for a, i in enumerate(list1):
	if i % 2 == 0:
		print(i, end=" ")

#2
list1 = [2, 7, 5, 64, 14]
for i in list1:
	if (i % 2 != 0):
		pass
	else:
		print(i, end=" ")


#3
# Python code To print all even numbers
# in a given list using numpy array
import numpy as np

# Declaring Range
temp = [2, 7, 5, 64, 14]
li = np.array(temp)

# printing even numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)

#4
#python program to print all even no's in a list
#defining list with even and odd numbers 
list1=[39,28,19,45,33,74,56] 
#traversing list using for loop
for element in list1:
if not element&1: #condition to check even or not
	print(element,end=' ')


#5
# Python program to print all even no's in a list


# Defining list with even and odd numbers
# Initializing list 
list1=[39,28,19,45,33,74,56]

# Traversing list using for loop
for element in list1:
	
	# condition to check even or not
	if element|1 != element: 
		print(element,end=' ')

#6
import numpy as np

# given list
list1 = [2, 7, 5, 64, 14]

# converting list to numpy array
arr = np.array(list1)

# finding even numbers using where() method
even_num = arr[np.where(arr % 2 == 0)]

# printing even numbers
print(even_num)

#7
# Using the filterfalse function from the itertools module
from itertools import filterfalse

# Test list1
list1 = [39, 28, 19, 45, 33, 74, 56]

# filtering even number
even_numbers = filterfalse(lambda y: y % 2, list1)

# Printing result
for num in even_numbers:
	print(num, end=" ")

#8
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 != 0:
	print(num, end=" ")

#9
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
i = 0

# using while loop
while(i < len(list1)):

	# checking condition
	if list1[i] % 2 != 0:
		print(list1[i], end=" ")

	# increment i
	i += 1

#10
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

only_odd = [num for num in list1 if num % 2 == 1]

print(only_odd)

#11
#List of numbers
list1 = [9,5,4,7,2]

for ele in list1:
if ele & 1: #Checking the element odd or not
	print(ele,end=" ") 


#12
#List of numbers
list1 = [9,5,4,7,2]

for ele in list1:
if ele | 1==ele: #Checking the element odd or not
	print(ele,end=" ") 

#13
def is_odd(number):
return number % 2 == 1

def print_odd_numbers(numbers):
odd_numbers = list(filter(is_odd, numbers))
return odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(print_odd_numbers(numbers))

#14
import numpy as np

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# convert list to numpy array
arr = np.array(list1)

# find indices where elements are odd
idx = np.where(arr % 2 != 0)

# extract elements at odd indices
only_odd = arr[idx]

# print only odd elements
print(only_odd)

#15
