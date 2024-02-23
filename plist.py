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

		