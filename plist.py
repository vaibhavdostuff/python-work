#1

list1 = [2, 7, 5, 64, 14]
for a, i in enumerate(list1):
	if i % 2 == 0:
		print(i, end=" ")

#2 
# To print all even numbers
# in a given list using numpy array
import numpy as np

# Declaring Range
temp = [2, 7, 5, 64, 14]
li = np.array(temp)

# printing even numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)

#4

# to print all even no's in a list
# defining list with even and odd numbers 
list1=[39,28,19,45,33,74,56] 
#traversing list using for loop
for element in list1:
 if not element&1: #condition to check even or not
	 print(element,end=' ')

#5


# Initializing list 
list1=[19,28,39,15,43,74,66]

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

# to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 != 0:
	 print(num, end=" ")

#9

# to print odd Numbers in a List

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

# to print odd Numbers in a List

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

# to print odd Numbers in a List
from functools import reduce

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# Using reduce method in list
odd_list = reduce(lambda a, b : a + [b] if b%2 else a, list1, [])

print(odd_list)

#16

# to print all even numbers in range
for even_numbers in range(4,15,2):
#here inside range function first no denotes starting,
#second denotes end and
#third denotes the interval
	print(even_numbers,end=' ')


#17

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

#18


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

# in a given range using the lambda function
a=6;b=20
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

# To print all even numbers
# in a given range using numpy array
import numpy as np

# Declaring Range
a=4;b=15
li= np.array(range(a, b+1))

# printing odd numbers using numpy array
even_num = li[li%2==0];
print(even_num)

#25

# to print odd Numbers in given range

start, end = 4, 19

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num % 2 != 0:
		print(num, end = " ")

#26

# to print Even Numbers in given range

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

# iterating each number in list
for num in range(start, end + 1):

	# checking condition
	if num % 2 != 0:
		print(num)

#27

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

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

# to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#create a list that contains only Even numbers in given range
even_list = range(start, end + 1)[start%2::2]

for num in even_list:
	print(num, end = " ")

#29

# To print all odd numbers 
# in a given range using the lambda function
a=3;b=11
li=[]
for i in range(a,b+1):
	li.append(i)
# printing odd numbers using the lambda function
odd_num = list(filter(lambda x: (x%2!=0),li)) 
print(odd_num)

#30

def odd(num1,num2):
	if num1>num2:
		return
	if num1&1:
		print(num1,end=" ")
		return odd(num1+2,num2)
	else:
		return odd(num1+1,num2)
num1=5;num2=15
odd(num1,num2)


#31

x = [i for i in range(4,15+1) if i%2!=0]
print(*x)

#32

a=4;b=15;l=[]
for i in range(a,b+1):
 l.append(i)
 print([a for j,a in enumerate(l) if a%2!=0])

#33

a=2;b=7
for i in range(a,b+1):
 if i%2==0:
	 pass
else:
	print(i,end=" ")

#34

# to print Even Numbers in given range

# Range declaration
a=4;
b=15;

#create a list that contains only Even numbers in given range
l= filter(lambda a : a%2 , range(a, b+1))
print(*l)


#35

# to print odd Numbers in given range
# using bitwise | operator
start, end = 4, 19

# iterating each number in list

for num in range(start, end + 1):
	# checking condition

	if num | 1 == num:

		print(num, end = " ")

#36

# to demonstrate
# print odd number in range
import itertools

# Range declaration
a = 4
b = 20

# using filterfalse function 
evens = list(itertools.filterfalse(lambda x: x%2==0, range(a, b+1)))

# Print the array of even numbers
print(*evens)

#37

# to print Positive Numbers in a List

# list of numbers
list1 = [-10, 21, -4, 45, -6, 43]

# using list comprehension
pos_nos = [num for num in list1 if num >= 0]

print("Positive numbers in the list: ", *pos_nos)

#38


list1 = [11, -21, 0, 45, 66, -93]

# iterating each number in list
for num in list1:

	# checking condition
	if num & gt = 0:
		print("num, end= & quot & quot")

#39

list1 = [10, 21, -4, -45, -66, 33]
num = 0

# using while loop	 
while(num < len(list1)):
	
	# checking condition
	if list1[num] >= 0:
		print(list1[num], end = " ")
	
	# increment num 
	num += 1
	
#40

list1 = [-20, 21, 4, -45, 16, 93, -11] 


# we can also print positive no's using lambda exp. 
pos_nos = list(filter(lambda x: (x >= 0), list1))

print("Positive numbers in the list: ", *pos_nos) 

#41

l=[12, -7, 5, 64, -14]
print([a for j,a in enumerate(l) if a>=0])

#42


list1 = [11, -21, 0, 45, 66, -93]
res=[]
list2=list(map(str,list1))
for i in range(0,len(list2)):
	if( not list2[i].startswith("-") and list2[i] !="0"):
		res.append(str(list1[i]))
res=" ".join(res)
print(res)

#43

# to print Positive Numbers in a List
import numpy as np
# list of numbers
list1 = np.array([-10, -21, -4, 45, -66, 93])

# using numpy Array
pos_nos = list1[list1 >=0];

print("Positive numbers in the list: ", *pos_nos)

#44

# to print positive Numbers in a List

# list of numbers
list1 = [-10, 21, 4, -45, -66, 93, -11]

import operator
pos_nos = []
for i in list1:
	if operator.ge(i,0):
		pos_nos.append(i)

print("Positive numbers in the list: ", pos_nos)

#45

# to print negative Numbers in a List

# list of numbers
list1 = [11, -21, 0, 45, 66, -93]

# iterating each number in list
for num in list1:

	# checking condition
	if num < 0:
	 print(num, end=" ")

#46

list1 = [-10, 21, -4, -25, 36, 48]
num = 0

# using while loop
while(num < len(list1)):
	# checking condition
	if list1[num] < 0:
		print(list1[num] , end=" ")

	# increment num
	num += 1

#47

# to print negative Numbers in a List

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
neg_nos = [num for num in list1 if num < 0]

print("Negative numbers in the list: ", *neg_nos)

#48


list1 = [-10, 21, 4, -45, -66, 93, -11]


# we can also print negative no's using lambda exp.
neg_nos = list(filter(lambda x: (x < 0), list1))

print("Negative numbers in the list: ", *neg_nos)

#49

l=[12, -7, 5, 64, -14]
print([a for j,a in enumerate(l) if a<0])

#50


list1 = [11, -21, 0, 45, 66, -93]
res = []
list2 = list(map(str, list1))
for i in range(0, len(list2)):
	if(list2[i].startswith("-")):
		res.append(str(list1[i]))
res = " ".join(res)
print(res)

#51

# to print negative Numbers in a List

import numpy as np
# list of numbers
list1 = [-10, 21, 4, -45, -66, 93, -11]


# Using numpy to print the negative number
temp = np.array(list1)
neg_nos = temp[temp <= 0]

print("Negative numbers in the list: ", *neg_nos)

#52

#Recursive function to check current element negative or not
def PrintNegative(itr,list1):
	if itr == len(list1): #base condition
		return
		if list1[itr] < 0: #check negative number or not
			print( list1[itr],end = " ")
			PrintNegative(itr+1,list1) #recursive function call

list1 = [-1,8,9,-5,7]
PrintNegative(0,list1)

#53

import numpy as np

# list of numbers
list1 = [12, -7, 5, 64, -14]

# converting list to numpy array
arr1 = np.array(list1)

# finding negative numbers in the array
neg_nums = arr1[np.where(arr1 < 0)]

# printing negative numbers
print("Negative numbers in the list: ", *neg_nums)

#54

# to print negative Numbers in a List
from functools import reduce

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using reduce method
neg_nos = reduce(lambda a, b : a + [ b ] if b < 0 else a ,list1, [])

print("Negative numbers in the list: ", *neg_nos)

#55

# to print positive Numbers in given range 

start, end = -4, 19

# iterating each number in list 
for num in range(start, end + 1): 

	# checking condition 
	if num >= 0: 
		print(num, end=" ") 

#56


start = int(input("Enter the start of range: ")) 
end = int(input("Enter the end of range: ")) 

# iterating each number in list 
for num in range(start, end + 1): 

	# checking condition 
	if num >= 0: 
		print(num, end=" ") 

#57

# in a given range using the lambda function 
a=-4;b=5
li=[] 
for i in range(a,b+1): 
	li.append(i) 
# printing positive numbers using the lambda function 
positive_num = list(filter(lambda x: (x>=0),li)) 
print(positive_num)

#58
 
a=-4;b=5
out=[i for i in range(a,b+1) if i>0] 
# print the all positive numbers 
print(*out) 

#59

a=-4;b=5;l=[] 
for i in range(a,b+1): 
	l.append(i) 
	print([a for j,a in enumerate(l) if a>=0]) 

#60

a=-10;b=15
for i in range(a,b+1): 
	if i<0: 
		pass
else: 
	print(i,end=" ") 


#61

def printPositives(start,end): #defining recursive function to print positives 
	if start==end:return #base condition 
	if start>=0: #check for positive number 
		print(start,end=' ') 
printPositives(start+1,end) # recursive calling 
a,b=-2,8
printPositives(a,b) #function calling 

#62

a = -4
b = 12

positive_nums = list(filter(lambda x: x >= 0, range(a, b+1))) 
print(positive_nums) 

#63

# To print all negative numbers in a given range 


def negativenumbers(a,b): 
# Checking condition for negative numbers 
# single line solution 
 out=[i for i in range(a,b+1) if i<0] 
# print the all negative numbers
 print(*out) 

# driver code 
# a -> start range 
a=-20
# b -> end range 
b=5
negativenumbers(a,b)

#64

start, end = -4, 19

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num < 0:
		print(num, end = " ")

#65

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num < 0:
		print(num, end = " ")

#66

# numbers in a given range using lambda function

# inputs
a=-4;b=5
li=[]
for i in range(a,b):
	li.append(i)
# printing negative numbers using the lambda function
negative_num = list(filter(lambda x: (x<0),li)) 
print(negative_num)

#67

a=-8;b=6;l=[]
for i in range(a,b+1):
	l.append(i)
print([a for j,a in enumerate(l) if a<0])

#68

a=-4;b=5
print([i for i in range(a,b+1) if i<0])

#69

a=-14;b=25
for i in range(a,b+1):
	if i>=0:
		pass
else:
	print(i,end=" ")

#70

#Recursive function to print Negative numbers
def PrintNegative(itr,end):
	if itr == end:#Base Condition
		return
		if itr < 0: #checking Negative or not
			print(itr,end=" ")
			PrintNegative(itr+1,end) #Recursive function call
			return

a = -5
b = 5
PrintNegative(a,b) 

#71

import numpy as np

# Taking input values for start and end of the range
start = -4
end = 5

# Creating an array using numpy.arange()
arr = np.arange(start, end+1)

# Filtering negative numbers using numpy.where()
neg_arr = arr[np.where(arr<0)]

# Printing the resulting array
print(neg_arr)

#72

#  to remove multiple
# elements from a list 

# creating a list
list1 = [11, 5, 17, 18, 23, 50] 

# Iterate each element in list
# and add them in variable total
for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)

# printing modified list
print("New list after removing all even numbers: ", list1)

#73


# creating a list
list1 = [10, 15, 7, 28, 23, 50] 

# will create a new list, 
# excluding all even numbers
list1 = [ elem for elem in list1 if elem % 2 != 0]

print(*list1)

#74


# creating a list
list1 = [1, 5, 37, 28, 42, 20] 

# removes elements from index 1 to 4
del list1[1:5]

print(*list1)

#75


# creating a list
list1 = [11, 5, 17, 18, 23, 50] 

# items to be removed
unwanted_num = {11, 5}

list1 = [ele for ele in list1 if ele not in unwanted_num]

# printing modified list
print("New list after removing unwanted numbers: ", list1)

#76

# creating a list
list1 = [1, 5, 37, 28, 42, 20] 

# given index of elements 

unwanted = [0, 3, 4]

for ele in sorted(unwanted, reverse = True): 
	del list1[ele]

# printing modified list
print (*list1)

#77

list1 = [11, 5, 17, 18, 23, 50] 

list1 = [ elem for i,elem in enumerate(list1) if elem % 2 != 0]

print(list1)

#78

import numpy as np

#creating a list
list1 = [12, 15, 3, 10]

#convert list to numpy array
arr = np.array(list1)

#indices of elements to be removed
remove_idx = [0, 2]

#use numpy.delete() to remove elements
new_arr = np.delete(arr, remove_idx)

#convert numpy array back to list
new_list = new_arr.tolist()

#print the results
print("Removed =", [list1[i] for i in remove_idx], ", New_List =", new_list)

#79

# to Demonstrate Remove empty List
# from List using list comprehension

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using list comprehension
res = [ele for ele in test_list if ele != []]

# printing result
print("List after empty list removal : " + str(res))

#80

# from List using filter() Method

# Initializing list by custom values
test_list = [5, 6, [], 3, [], [], 9]

# Printing original list
print("The original list is : " + str(test_list))

# Removing empty List from List
# using filter() method
res = list(filter(None, test_list))

# Printing the resultant list
print("List after empty list removal : " + str(res))

#81

# to Remove empty List from List

def empty_list_remove(input_list):
	new_list = []
	for ele in input_list:
		if ele:
			new_list.append(ele)
	return new_list


# input list values
input_list = [5, 6, [], 3, [], [], 9]

# print initial list values
print(f"The original list is : {input_list}")
# function-call & print values
print(f"List after empty list removal : {empty_list_remove(input_list)}")

#82

# to Demonstrate Remove empty List

# Initializing list
test_list = [10, 6, [], 3, [], [], 4]

# printing original list
print("The original list is : " + str(test_list))
new_list=[]
# Remove empty List from List
for i in test_list:
	x=str(type(i))
	if(x.find('list')!=-1):
		if(len(i)!=0):
			new_list.append(i)
	else:
		new_list.append(i)
# printing result
print("List after empty list removal : " + str(new_list))

#83


# Initializing list
test_list = [5, 8, [], 12, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
while [] in test_list :
	test_list.remove([])

# printing result
print("List after empty list removal : " + str(test_list))


#84

# Initializing list
test_list = [10, 6, [], 7, [], [], 4]

# printing original list
print("The original list is : " + str(test_list))
x=list(map(str,test_list))
y="".join(x)
y=y.replace("[]","")
y=list(map(int,y))

# printing result
print("List after empty list removal : " + str(y))


#85

test_list = [5, 6, [], 3, [], [], 9]
res = [ele for i,ele in enumerate(test_list) if ele != []]
print(res)

#86


# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
res = filter(None, test_list)

# printing result
print("List after empty list removal : " ,res)


#87

# from List using lambda function

# Initializing list by custom values
test_list = [15, 26, [], 8, [], [], 10]

# Printing original list
print("The original list is : " + str(test_list))

# Removing empty List from List
# using lambda function
res = list(filter(lambda x: x != [], test_list))

# Printing the resultant list
print("List after empty list removal : " + str(res))


#88 

#defining recursive function to remove empty list 
def remove_empty(start,oldlist,newlist):
	if start==len(oldlist): #base condition 
		return newlist
		if oldlist[start]==[]: #checking the element is empty list or not
			pass
		else:
			newlist.append(oldlist[start]) #appending non empty list element to newlist
			return remove_empty(start+1,oldlist,newlist) #recursive function call

test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))
result=remove_empty(0,test_list,[])
# printing result
print("List after empty list removal : " ,result)

#89


import itertools

# Initializing list by custom values
test_list = [5, 6, [], 3, [], [], 9]

# Printing original list
print("The original list is : " + str(test_list))

# Removing empty List from List
# using lambda function
res = list(itertools.filterfalse(lambda x: x == [], test_list))

# Printing the resultant list
print("List after empty list removal : " + str(res))


#90

import re

# input list values
input_list = [5, 6, [], 3, [], [], 9]

# print initial list values
print(f"The original list is : {input_list}")

# removing empty list from list
res = list(filter(None, [x for x in input_list if not re.match('\[\]', str(x))]))

# print resultant list
print(f"List after empty list removal : {res}")

