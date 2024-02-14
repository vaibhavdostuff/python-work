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
