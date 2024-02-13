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

