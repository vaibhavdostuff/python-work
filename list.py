#1

# to swap first
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
newList = [22, 35, 10, 56, 34]

print(swapList(newList))

#2

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [22, 45, 9, 56, 54]
print(swapList(newList))



#3

# Swap function
def swapList(list):
	
	start, *middle, end = list
	list = [end, *middle, start]
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#4

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

#5

# program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))


#6

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

#7


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

#8

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


#9

# program to illustrate 
# the usage of * operand
list = [1, 2, 3, 4]

a, *b, c = list

print(a)
print(b)
print(c)


#10

# Python len()
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)

#11

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



#12

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

#13

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


#14

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


#15

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


#16

# Define the list to be used for the demonstration
test_list = [1, 4, 5, 7, 8]

# Calculate the length of the list using a list comprehension and the sum function
# The list comprehension generates a sequence of ones for each element in the list
# The sum function then sums all the ones to give the length of the list
length = sum(1 for _ in test_list)

# Print the length of the list
print("Length of list using list comprehension is:", length)


#17

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


#18

# to find the length
# of list using enumerate function
list1 = [1, 4, 5, 7, 8]
s = 0
for i, a in enumerate(list1):
	s += 1
print(s)


#19

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

#20

lst=[ 2, 6, 9, 8, 3, 4 ] 
#checking if element 7 is present
# in the given list or not
i=7
# if element present then return
# exist otherwise not exist
if i in lst: 
	print("exist") 
else: 
	print("not exist")


#21

# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

# Checking if 4 exists in list
for i in test_list:
	if(i == 4):
		print("Element Exists")
	

#22

# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))


#23

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


#24

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


#25

# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")
x=list(map(str,test_list))
y="-".join(x)

if y.find("15") !=-1:
	print("Yes, 15 exists in list")
else:
	print("No, 15 does not exists in list")


#26

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

word = [8, 0, 2, 1]
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
list2 = [7, 8, 9]

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


lst = [1, 2, 3, 4, 5]

print("List before clearing: ",lst)
# Clearing list using slicing
lst = lst[:0]
print("List after clearing using Slicing: ",lst)


#37

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


# Using the in-built function extend()


def Cloning(li1):
	li_copy = []
	li_copy.extend(li1)
	return li_copy


# Driver Code
li1 = [6, 10, 4, 9, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


#39


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


# Using list comprehension 
lst = [4, 8, 2, 10, 15, 18] 
li_copy = [i for a,i in enumerate(lst)] 
print("Original List:", lst) 
print("After Cloning:", li_copy) 


#46

# Using map function
lst = [4, 8, 2, 10, 15, 18]
li_copy = map(int, lst)
print("Original List:", lst)
print("After Cloning:", *li_copy)


#47

from collections import deque

original_list = [4, 8, 2, 10, 15, 18]

copied_list = deque(original_list)
copied_list = list(copied_list)

print("Original List:", original_list)

print("After Cloning:", copied_list)


#48

# to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))


#49

l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
ele=1
x=[i for i in l if i==ele] 
print("the element",ele,"occurs",len(x),"times")


#50

l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
ele=1
x=[i for j,i in enumerate(l) if i==ele] 
print("the element",ele,"occurs",len(x),"times")


#51

# to count the number of occurrences
def countX(lst, x):
	return lst.count(x)


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, 
										countX(lst, x)))


#52

from collections import Counter

# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))


#53

import operator as op

# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 2
print(f"{x} has occurred {op.countOf(l, x)} times")


#54

lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
occurrence = {item: lis.count(item) for item in lis}
print(occurrence.get('e'))


#55

import pandas as pd

# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

count = pd.Series(l).value_counts()
print("Element Count")
print(count)


#56

# to remove empty tuples from a 
# list of tuples function to remove empty tuples 
# using list comprehension
def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
		('krishna', 'sudhama', '45'), ('',''),()]
print(Remove(tuples))


#57

# from a list of tuples function to remove 
# empty tuples using filter
def Remove(tuples):
	tuples = filter(None, tuples)
	return tuples
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'sudhama', '45'), ('',''),()]
print Remove(tuples)


#58

# a list of tuples function to remove empty
# tuples using filter


def Remove(tuples):
	tuples = filter(None, tuples)
	return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'sudhama', '45'), ('', ''), ()]
print(Remove(tuples))


#59

# to remove empty tuples from a
# list of tuples function to remove empty tuples
# using len()


def Remove(tuples):
	for i in tuples:
		if(len(i) == 0):
			tuples.remove(i)
	return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'sudhama', '45'), ('', ''), ()]
print(Remove(tuples))


#60

# list of tuples function to remove empty tuples
def Remove(tuples):
	for i in tuples:
		if(i==()):
			tuples.remove(i)
			return tuples
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'sudhama', '45'), ('',''),()]
print(Remove(tuples))

#61

tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'sudhama', '45'), ('', ''), ()]
res = [t for i, t in enumerate(tuples) if t]
print(res)


#62

# to remove empty tuples from
# a list of tuples function to remove empty
# tuples using while loop and in operator 
def Remove(tuples):
	while () in tuples:
		tuples.remove(());
	return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()]
print (Remove(tuples))


#63

# list of tuples function to remove empty tuples


def Remove(tuples):
	for i in tuples:
		if(str(i).find("()") != -1 and len(str(i)) == 2):
			tuples.remove(i)
	return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))


#64

# a list of tuples function to remove empty
# tuples using lambda function


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('', ''), ()]

tuples = list(filter(lambda x: len(x) > 0, tuples))
print(tuples)


#65

import itertools # import the itertools module

def Remove(tuples):
	tuples = list(itertools.filterfalse(lambda x: x == (), tuples)) # remove empty tuples using filterfalse from itertools
	return tuples

# Driver code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()] # define the input list of tuples
print(Remove(tuples)) # call the Remove function and print the output


#66

# Python program to print duplicates from 
# a list of integers
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniqueList = []
duplicateList = []

for i in lis:
	if i not in uniqueList:
		uniqueList.append(i)
	elif i not in duplicateList:
		duplicateList.append(i)

print(duplicateList)


#67

from collections import Counter

l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)

#68

lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
	if i not in x:
		x.append(i)
for i in x:
	if lis.count(i) > 1:
		y.append(i)
print(y)


#69

input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print(list(set([x for i,x in enumerate(input_list) if input_list.count(x) > 1])))


#70

lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
import operator
for i in lis:
	if i not in x:
		x.append(i)
for i in x:
	if operator.countOf(lis,i) > 1:
		y.append(i)
print(y)


#71

#  to get the Cumulative sum of a list 
def Cumulative(lists): 
	cu_list = [] 
	length = len(lists) 
	cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)] 
	return cu_list[1:]

# Driver Code 
lists = [10, 20, 30, 40, 50] 
print (Cumulative(lists)) 


#72

from itertools import accumulate
import operator

def cumulative_sum(input_list):
	# Use the accumulate() function to perform a cumulative sum of the elements in the list
	cumulative_sum_iter = accumulate(input_list, operator.add)
	# Convert the iterator to a list and return it
	return list(cumulative_sum_iter)

input_list = [10, 20, 30, 40, 50]
output_list = cumulative_sum(input_list)
print(output_list)


#73

import numpy as np

def cumulative_sum(input_list):
	# Convert the list to a NumPy array
	input_array = np.array(input_list)
	# Compute the cumulative sum along the first axis of the array
	cumulative_sum_array = np.cumsum(input_array)
	# Convert the NumPy array back to a list and return it
	return cumulative_sum_array.tolist()

input_list = [10, 20, 30, 40, 50]
output_list = cumulative_sum(input_list)
print(output_list)


#74

from collections import Counter

def cumulative_sum(lst):
	cnt = Counter(lst)
	cum_sum = [lst[0]]
	for i in range(1, len(lst)):
		cum_sum.append(cum_sum[i-1] + lst[i])
	return cum_sum

lst = [10, 20, 30, 40, 50]
result = cumulative_sum(lst)
print(result)


#75

# to demonstrate Sum of number digits in List
# using loop + str()

# Initializing list
test_list = [32, 57, 98, 44]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using loop + str()
res = []
for ele in test_list:
	sum = 0
	for digit in str(ele):
		sum += int(digit)
	res.append(sum)
	
# printing result 
print ("List Integer Summation : " + str(res))


#76

# using sum() + list comprehension

# Initializing list
test_list = [12, 67, 78, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
	
# printing result 
print ("List Integer Summation : " + str(res))


#77

# using sum() + reduce()
from functools import reduce

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + reduce()
res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]

# printing result
print("List Integer Summation : " + str(res))


#78

import numpy as np

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using numpy
res = np.sum([list(map(int, str(ele))) for ele in test_list], axis=1)

# printing result
print("List Integer Summation : " + str(list(res)))


#79

lst = [12, 67, 98, 34]
def digit_sum(num):
	digit_sum = 0
	while num > 0:
		digit_sum += num % 10
		num //= 10
	return digit_sum

def sum_of_digits_list(lst):
	return list(map(digit_sum, lst))

print(sum_of_digits_list(lst))


#80

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# creating an expression
res = list(sum(int(digit) for digit in str(num)) for num in test_list)
# printing result
print("List Integer Summation : " + str(list(res)))