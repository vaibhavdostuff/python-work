#1
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#2
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#3
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	# Storing the first and last element 
	# as a pair in a tuple variable get
	get = list[-1], list[0]
	
	# unpacking those elements
	list[0], list[-1] = get
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#4
# Python3 program to illustrate 
# the usage of * operand
list = [1, 2, 3, 4]

a, *b, c = list

print(a)
print(b)
print(c)

#5
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	start, *middle, end = list
	list = [end, *middle, start]
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#6
def swap_first_last_3(lst):
	# Check if list has at least 2 elements
	if len(lst) >= 2:
		# Swap the first and last elements using slicing
		lst = lst[-1:] + lst[1:-1] + lst[:1]
	return lst

# Initializing the input
inp=[12, 35, 9, 56, 24]

# Printing the original input
print("The original input is:",inp)

result=swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:",result)

#10
# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))


#11
# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	# popping both the elements from list
	first_ele = list.pop(pos1) 
	second_ele = list.pop(pos2-1)
	
	# inserting in each others positions
	list.insert(pos1, second_ele) 
	list.insert(pos2, first_ele) 
	
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))

#12
# Python3 program to swap elements at
# given positions

# Swap function
def swapPositions(list, pos1, pos2):

	# Storing the two elements
	# as a pair in a tuple variable get
	get = list[pos1], list[pos2]
	
	# unpacking those elements
	list[pos2], list[pos1] = get
	
	return list

# Driver Code
List = [23, 65, 19, 90]

pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))

#13
# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(lis, pos1, pos2):
	temp=lis[pos1]
	lis[pos1]=lis[pos2]
	lis[pos2]=temp
	return lis
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))

#14
# Python len()
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)

#15
# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list using loop
# Initializing counter
counter = 0
for i in test_list:

	# incrementing counter
	counter = counter + 1

# Printing length of list
print("Length of list using naive method is : " + str(counter))

#16
from operator import length_hint

# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list using len()
list_len = len(test_list)

# Finding length of list using length_hint()
list_len_hint = length_hint(test_list)

# Printing length of list
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len_hint))

#17
# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list
# using sum()
list_len = sum(1 for i in test_list)


# Printing length of list
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len))

#18
from operator import length_hint

# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list using len()
list_len = len(test_list)

# Finding length of list using length_hint()
list_len_hint = length_hint(test_list)

# Printing length of list
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len_hint))

#19
# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list
# using sum()
list_len = sum(1 for i in test_list)


# Printing length of list
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len))

#20
# Define the list to be used for the demonstration
test_list = [1, 4, 5, 7, 8]

# Calculate the length of the list using a list comprehension and the sum function
# The list comprehension generates a sequence of ones for each element in the list
# The sum function then sums all the ones to give the length of the list
length = sum(1 for _ in test_list)

# Print the length of the list
print("Length of list using list comprehension is:", length)

#21
# Define a function to count the number of elements in a list using recursion
def count_elements_recursion(lst):
	# Base case: if the list is empty, return 0
	if not lst:
		return 0
	# Recursive case: add 1 to the count of the remaining elements in the list
	return 1 + count_elements_recursion(lst[1:])


# Test the function with a sample list
lst = [1, 2, 3, 4, 5]
print("The length of the list is:", count_elements_recursion(lst))

#22
# python code to find the length
# of list using enumerate function
list1 = [1, 4, 5, 7, 8]
s = 0
for i, a in enumerate(list1):
	s += 1
print(s)

#23
from operator import length_hint
import time

# Initializing list
test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list
# using loop
# Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:

	# incrementing counter
	counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)

# Finding length of list
# using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)

# Finding length of list
# using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)

# Printing Times of each
print("Time taken using naive method is : " + end_time_naive)
print("Time taken using len() is : " + end_time_len)
print("Time taken using length_hint() is : " + end_time_hint)

#24
lst=[ 1, 6, 3, 5, 3, 4 ] 
#checking if element 7 is present
# in the given list or not
i=7
# if element present then return
# exist otherwise not exist
if i in lst: 
	print("exist") 
else: 
	print("not exist")

#25
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

# Checking if 4 exists in list
for i in test_list:
	if(i == 4):
		print("Element Exists")
	
#26
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))

#27
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")

# number of times element exists in list
exist_count = test_list.count(15)

# checking if it is more than 0
if exist_count > 0:
	print("Yes, 15 exists in list")
else:
	print("No, 15 does not exists in list")

#28
from bisect import bisect_left ,bisect

# Initializing list 
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using set() + in) : ")

# Checking if 4 exists in list 
# using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set :
	print ("Element Exists")

print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")

# Checking if 4 exists in list 
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4)!=bisect(test_list_bisect, 4):
	print ("Element Exists")
else:
	print("Element doesnt exist")

#29
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")
x=list(map(str,test_list))
y="-".join(x)

if y.find("15") !=-1:
	print("Yes, 15 exists in list")
else:
	print("No, 15 does not exists in list")

#30
from collections import Counter

test_list = [10, 15, 20, 7, 46, 2808]

# Calculating frequencies
frequency = Counter(test_list)

# If the element has frequency greater than 0
# then it exists else it doesn't exist
if(frequency[15] > 0):
	print("Yes, 15 exists in list")
else:
	print("No, 15 does not exists in list")

#31
word = [6, 0, 4, 1]
print('word before clear:', word)

# Clearing list
word.clear()
print('word after clear:', word)

#32
list1 = [1, 2, 3]

# Printing list2 before deleting
print("List1 before deleting is : "
	+ str(list1))

# deleting list using reinitialization
list1 = []

# Printing list2 after reinitialization
print("List1 after clearing using reinitialization : "
	+ str(list1))

#33
# Initializing lists
list1 = [1, 2, 3]

# Printing list2 before deleting
print("List1 before clearing is : "
	+ str(list1))

list1*=0
# Printing list2 after reinitialization
print("List1 after clearing using *=0 : "
	+ str(list1))

#34
list1 = [1, 2, 3]
list2 = [5, 6, 7]

# Printing list1 before deleting
print("List1 before deleting is : " + str(list1))

# deleting list1 using del
del list1[:]
print("List1 after clearing using del : " + str(list1))


# Printing list2 before deleting
print("List2 before deleting is : " + str(list2))

# deleting list using del
del list2[:]
print("List2 after clearing using del : " + str(list2))

#35
list1 = [1, 2, 3]

# Printing list1 before deleting
print("List1 before deleting is : " + str(list1))

# deleting list1
while(len(list1) != 0):
	list1.pop()
print("List1 after clearing using del : " + str(list1))

#36
# Initializing list
lst = [1, 2, 3, 4, 5]

print("List before clearing: ",lst)
# Clearing list using slicing
lst = lst[:0]
print("List after clearing using Slicing: ",lst)

#37
# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
	li_copy = li1[:]
	return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#38
# Python code to clone or copy a list
# Using the in-built function extend()


def Cloning(li1):
	li_copy = []
	li_copy.extend(li1)
	return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#39
# Python code to clone or copy a list 
# Using the List copy using =
def Cloning(li1): 
	li_copy = li1
	return li_copy 

# Driver Code 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2)

#40
# importing copy module
import copy

# initializing list 1 
li1 = [1, 2, [3,5], 4]

# using copy for shallow copy 
li2 = copy.copy(li1)

print(li2)

#41
# Python code to clone or copy a list 
# Using list comprehension 
def Cloning(li1): 
	li_copy = [i for i in li1] 
	return li_copy 

# Driver Code 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2) 

#42
# Python code to clone or copy a list 
# Using append() 
def Cloning(li1): 
	li_copy =[] 
	for item in li1: li_copy.append(item) 
	return li_copy 

# Driver Code 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2)

#43
# Python code to clone or copy a list 
# Using built-in method copy() 
def Cloning(li1): 
	li_copy =[] 
	li_copy = li1.copy() 
	return li_copy 

# Driver Code 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2)

#44
# importing copy module
import copy

# initializing list 1 
li1 = [1, 2, [3,5], 4]

# using deepcopy for deepcopy 
li3 = copy.deepcopy(li1) 
print(li3)

#45
