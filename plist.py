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
# Python program to print odd Numbers in a List
from functools import reduce

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# Using reduce method in list
odd_list = reduce(lambda a, b : a + [b] if b%2 else a, list1, [])

print(odd_list)

#16
# Python program to print all even numbers in range
for even_numbers in range(4,15,2):
#here inside range function first no denotes starting,
#second denotes end and
#third denotes the interval
	print(even_numbers,end=' ')


#17
# Python program to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

#18
# Python program to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#creating even starting range
start = start+1 if start&1 else start


#create a list and printing element
#contains Even numbers in range
[ print( x ) for x in range(start, end + 1, 2)]

#19
def even(num1,num2):
	if num1>num2:
		return
	print(num1,end=" ")
	return even(num1+2,num2)
num1=4;num2=15
even(num1,num2)

#20
# Python code To print all even numbers 
# in a given range using the lambda function
a=4;b=15
li=[]
for i in range(a,b+1):
	li.append(i)
# printing odd numbers using the lambda function
even_num = list(filter(lambda x: (x%2==0),li)) 
print(even_num)

#21
x=[i for i in range(4,15+1) if i%2==0]
print(*x)

#22
a=4;b=15;l=[]
for i in range(a,b+1):
l.append(i)
print([a for j,a in enumerate(l) if a%2==0])

#23
a=4;b=15
for i in range(a,b+1):
if i%2!=0:
	pass
else:
	print(i,end=" ")

#24
# Python code To print all even numbers
# in a given range using numpy array
import numpy as np

# Declaring Range
a=4;b=15
li= np.array(range(a, b+1))

# printing odd numbers using numpy array
even_num = li[li%2==0];
print(even_num)

#25
# Python program to print odd Numbers in given range

start, end = 4, 19

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num % 2 != 0:
		print(num, end = " ")

#26
# Python program to print Even Numbers in given range

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

# iterating each number in list
for num in range(start, end + 1):

	# checking condition
	if num % 2 != 0:
		print(num)

#27
# Uncomment the below two lines for taking the User Inputs
#start = int(input("Enter the start of range: "))
#end = int(input("Enter the end of range: "))

# Range declaration
start = 5
end = 20

if start % 2 != 0:

	for num in range(start, end + 1, 2):
		print(num, end=" ")
else:

	for num in range(start+1, end + 1, 2):
		print(num, end=" ")

#28
# Python program to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#create a list that contains only Even numbers in given range
even_list = range(start, end + 1)[start%2::2]

for num in even_list:
	print(num, end = " ")

#29