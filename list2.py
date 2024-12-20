#1

# Reversing a list using slicing technique
def Reverse(lst):
 new_lst = lst[::-1]
 return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#2

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))

#3

# Reversing a list using two-pointer approach
def reverse_list(arr):
	left = 0
	right = len(arr)-1
	while (left < right):
		# Swap
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left += 1
		right -= 1

	return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))

#4

# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = [] # empty list

# iterate to reverse the list
for i in lst:
	# reversing the list
	l.insert(0, i)
# printing result
print(l)

#5

original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
			for i in range(1, len(original_list)+1)]
print(new_list)

#6

import numpy as np

# Input list
my_list = [5, 6, 7, 8, 9, 10]

# Convert the list to a 1D numpy array
my_array = np.array(my_list)

# Reverse the order of the array
reversed_array = my_array[::-1]

# Convert the reversed array to a list
reversed_list = reversed_array.tolist()

# Print the reversed list
print(reversed_list)

#7

# to find sum of elements in list

total = 0

# creating a list
list1 = [11, 50, 27, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)

#8

total = 0
ele = 0

# creating a list
list1 = [1, 35, 47, 18, 43] 

# Iterate each element in list
# and add them in variable total
while(ele < len(list1)):
	total = total + list1[ele]
	ele += 1
	
# printing total value
print("Sum of all elements in given list: ", total)

#9

# elements in list using recursion

# creating a list
list1 = [11, 5, 17, 18, 23]

# creating sum_list function


def sumOfList(list, size):
	if (size == 0):
		return 0
	else:
		return list[size - 1] + sumOfList(list, size - 1)


# Driver code
total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)

#10

# creating a list
list1 = [10, 5, 27, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print("Sum of all elements in given list: ", total)

#11

# using add function of operator module

from operator import*
list1 = [12, 5, 8, 10]
result = 0
for i in list1:
# Adding elements in the list using
# add function of operator module
	result = add(i, result)
# printing the result
print(result)

#12

list1 = [12, 15, 3, 10];s=0
for i,a in enumerate(list1): 
s+=a 
print(s)

#13

list1 = [12, 15, 3, 10]
s=[i for i in list1] 
print(sum(s))

#14

list1 = [22, 25, 33, 19]
print(sum(list(filter(lambda x: (x),list1))))

#15

import operator
list1 = [12, 15, 3, 10] ;s=0
for i in list1:
s=s+operator.add(0,i)
print(s)

#16

# to multiply all values in the
# list using traversal


def multiplyList(myList):

	# Multiply elements one by one
	result = 1
	for x in myList:
		result = result * x
	return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

#17

# list using numpy.prod()

import numpy
list1 = [1, 2, 3]
list2 = [3, 2, 4]

# using numpy.prod() to get the multiplications
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)

#18

# list using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

#19

# list using math.prod
import math
list1 = [1, 2, 3] 
list2 = [3, 2, 4]

result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)

#20

# the given list by importing operator module

from operator import*
list1 = [1, 2, 3]
m = 1
for i in list1:
# multiplying all elements in the given list 
# using mul function of operator module
	m = mul(i, m)
# printing the result
print(m)

#21

def multiply_list(list1):
	# Initialize product to 1
	product = 1
	
	# Iterate through each element in the list
	for element in list1:
		product *= element
	
	return product

# Example
list1 = [1, 2, 3, 4, 5]
result = multiply_list(list1)
print(result)

#22

# list using traversal

def multiplyList(myList) :
	
	# Multiply elements one by one
	result = 1
	for i in range(0,len(myList)):
		result = result * myList[i]
	return result
	
# Driver code
list1 = [1, 2, 3]
list2 = [5, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

#23

# list using lambda function and accumulate()
from itertools import accumulate
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = list(accumulate(list1, (lambda x, y: x * y)))
result2 = list(accumulate(list2, (lambda x, y: x * y)))
print(result1[-1])
print(result2[-1])

#24

def product_recursive(numbers):
	# base case: list is empty
	if not numbers:
		return 1
	# recursive case: multiply first element by product of the rest of the list
	return numbers[0] * product_recursive(numbers[1:])
list1 = [1, 2, 3]
product = product_recursive(list1)
print(product) # Output: 6

list2 = [3, 2, 4]
product = product_recursive(list2)
print(product) # Output: 24

#25

from functools import reduce
from operator import mul

list1 = [4, 5, 6]
result = reduce(mul, list1)

print(result)

#26

# to find smallest 
# number in a list

# list of numbers
list1 = [10, 20, 4, 35, 29]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", list1[0])

#27


list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort(reverse=True)

# printing the first element
print("Smallest element is:", list1[-1])

#28


# list of numbers
list1 = [10, 20, 1, 45, 99]


# printing the minimum element
print("Smallest element is:", min(list1))

#29


# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
	ele= int(input("Enter elements: "))
	list1.append(ele)
	
# print minimum element:
print("Smallest element is:", min(list1))

#30



l=[ int(l) for l in input("List:").split(",")]
print("The list is ",l)

# Assign first element as a minimum.
min1 = l[0]

for i in range(len(l)):

	# If the other element is min than first element
	if l[i] < min1: 
		min1 = l[i] #It will change

print("The smallest element in the list is ",min1)

#31


lst = [20, 10, 20, 1, 100]
print(min(lst, key=lambda value: int(value)) )

#32

lst = [20, 40, 20, 18, 30] 
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)

#33

# to print smallest element in the list
from functools import reduce
lst = [20, 10, 20, 25, 30]
print(reduce(min,lst) )

#34

# defining the list
arr = [5,2,3,2,5,4,7,9,7,10,9,48]

# converting the list into set
set_arr = set(arr)

# Now using the min function to get the minimum
# value from the set

print(min(set_arr))

#35

arr = [2,6,8,4,9,7,5,3,6,2,4,5,6,8,2]

min_val = min(arr) # Finding the minimum value

values = {}
# print item with position
for pos,val in enumerate(arr):
	if val==min_val:
		values.update({pos:val}) # pos - Index of the smallest element
								# val - The value of the smallest element

# get all min values
print(values)

#36

# to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 15, 9]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])

#37

# List of numbers
list1 = [10, 22, 14, 45, 9]

# Printing the maximum element
print("Largest element is:", max(list1))

#38


def myMax(list1):

	# Assume first number in list is largest
	# initially and assign it to variable "max"
	max = list1[0]
# Now traverse through the list and compare
	# each number with "max" value. Whichever is
	# largest assign that value to "max'.
	for x in list1:
		if x > max:
			max = x

	# after complete traversing the list
	# return the "max" value
	return max


# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))


#39

#  to print largest element in the list

lst = [20, 10, 20, 4, 100]
print(max(lst, key=lambda value: int(value)) )

#40

from functools import reduce
lst = [30, 10, 20, 40, 100]
largest_elem = reduce(max, lst)
print(largest_elem)

#41

# Function to find the largest element in the list
def FindLargest(itr, ele, list1):

# Base condition
	if itr == len(list1):
		print("Largest element in the list is: ", ele)
		return

	# Check max condition
	if ele < list1[itr]:
		ele = list1[itr]

		# Recursive solution
	FindLargest(itr+1, ele, list1)

	return

# input list
list1 = [2, 1, 7, 9, 5, 4]

FindLargest(0, list1[0], list1)

#42

import heapq

# list of numbers
list1 = [10, 20, 4, 45, 99]

# finding the largest element using heapq.nlargest()
largest_element = heapq.nlargest(1, list1)[0]

# printing the largest element
print("Largest element is:", largest_element)


#43

import numpy as np

# given list
list1 = [2, 7, 5, 64, 14]

# converting list to numpy array
arr = np.array(list1)

# finding largest numbers using np.max() method
num = arr.max()

# printing largest number
print(num)

#44

# to find second largest
# number in a list

# list of numbers - length of 
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2,n): 
	if list1[i] > mx: 
		secondmax = mx
		mx = list1[i] 
	elif list1[i] > secondmax and \
		mx != list1[i]: 
		secondmax = list1[i]
	elif mx == secondmax and \
		secondmax != list1[i]:
		secondmax = list1[i]

print("Second highest number is : ",\
	str(secondmax))

#45

# to find largest number
# in a list

# List of numbers
list1 = [10, 20, 20, 4, 45, 5, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])


#46

# to find second largest number
# in a list

# List of numbers
list1 = [10, 20, 4, 45, 99]

# new_list is a set of list1
new_list = set(list1)

# Removing the largest element from temp list
new_list.remove(max(new_list))

# Elements in original list are not changed
# print(list1)
print(max(new_list))


#47


# creating list of integer type
list1 = [10, 20, 4, 45, 99]

'''
# sort the list 
list1.sort()
	
# print second maximum element
print("Second largest element is:", list1[-2])

'''

# print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])

#48

def findLargest(arr):
	secondLargest = 0
	largest = min(arr)

	for i in range(len(arr)):
		if arr[i] > largest:
			secondLargest = largest
			largest = arr[i]
		else:
			secondLargest = max(secondLargest, arr[i])

	# Returning second largest element
	return secondLargest


# Calling above method over this array set
print(findLargest([10, 20, 4, 45, 99]))


#49

def secondmax(arr):
sublist = [x for x in arr if x < max(arr)]
return max(sublist)

if __name__ == '__main__':
arr = [10, 20, 4, 45, 99]
print(secondmax(arr))

#50

# to print second largest element in list

lst = [10, 20, 4, 45, 99]
maximum1 = max(lst)
maximum2 = max(lst, key=lambda x: min(lst)-1 if (x == maximum1) else x)
print(maximum2)

#51

lst = [10, 20, 40, 50, 90] 
m=max(lst)
x=[a for i,a in enumerate(lst) if a<m]
print(max(x))

#52

import heapq

def find_second_largest(numbers):
	# Build a max heap using the elements in the list
	heap = [(-x, x) for x in numbers]
	heapq.heapify(heap)
	
	# Remove the root element (largest element)
	heapq.heappop(heap)
	
	# The new root element is the second largest element
	_, second_largest = heapq.heappop(heap)
	
	return second_largest

# Test the function
numbers = [1, 22, 14, 25, 19]
print(find_second_largest(numbers))

#53

import numpy as np

def find_second_largest(arr):
	# creating numpy array
	np_arr = np.array(arr)

	# getting sorted indices
	sorted_indices = np.argsort(np_arr)

	# finding the second last index from sorted indices
	second_last_index = sorted_indices[-2]

	# returning the element at the second last index from original array
	return np_arr[second_last_index]

# example usage
arr = [18, 23, 41, 45, 32]
print(find_second_largest(arr)) 


#54

# to find N largest
# element from given list of integers

# Function returns N largest elements


def Nmaxelements(list1, N):
	final_list = []

	for i in range(0, N):
		max1 = 0

		for j in range(len(list1)):
			if list1[j] > max1:
				max1 = list1[j]

		list1.remove(max1)
		final_list.append(max1)

	print(final_list)


# Driver code
list1 = [2, 6, 41, 3, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)

#55


l = [1303, 298, 370, 100, 20, -45, 90]
n = 4

l.sort()
print(l[-n:])

#56

import heapq


def find_n_largest_elements(lst, N):
	heap = lst
	return heapq.nlargest(N, heap)


# Test the function with given inputs
lst = [4, 5, 1, 7, 9]
N = 2
print(find_n_largest_elements(lst, N))

lst = [61, 52, 45, 10, 3, 2, 56]
N = 3
print(find_n_largest_elements(lst, N))


#57

import numpy as np

def Nmaxelements(list1, N):
	list1 = np.array(list1) # convert list to numpy array
	return list1[np.argsort(list1)[-N:]]

list1 = [56, 6, 41, 85, 0, 3, 12, 6, 10]
N = 3
print(Nmaxelements(list1, N))


#58

# to print Even Numbers in a List

# list of numbers
list1 = [10, 47, 4, 55, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

#59


# Initializing list and value
list1 = [10, 24, 4, 45, 66, 93]
num = 0

# Uing while loop
while(num < len(list1)):

	# Cecking condition
	if list1[num] % 2 == 0:
		print(list1[num], end=" ")

	# increment num
	num += 1

#60


# Initializing list 
list1 = [10, 21, 4, 45, 66, 93]

# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)

#61


# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]


# we can also print even no's using lambda exp.
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)

#62

# even numbers in a list using recursion


def evennumbers(list, n=0):

	# base case
	if n == len(list):
		exit()
	if list[n] % 2 == 0:
		print(list[n], end=" ")
	
	# calling function recursively
	evennumbers(list, n+1)

# Initializing list 
list1 = [10, 21, 4, 45, 66, 93]

print("Even numbers in the list:", end=" ")
evennumbers(list1)

#63

my_list = ['vaibhav', 'is', 'here', 'like', 
		'fammily','nerdy', 'negi', 'love', 
			'questions','words', 'life'] 

# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
	
	# looping till length l 
	for i in range(0, len(l), n): 
		yield l[i:i + n] 

# How many elements each 
# list should have 
n = 5

x = list(divide_chunks(my_list, n)) 
print (x) 

#64

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
start = 0
end = len(my_list) 
step = 3
for i in range(start, end, step): 
	x = i 
	print(my_list[x:x+step]) 

#65

my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19] 

# How many elements each 
# list should have 
n = 4

# using list comprehension 
final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 
print (final) 

#66

l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# How many elements each 
# list should have 
n = 4

# using list comprehension 
x = [l[i:i + n] for i in range(0, len(l), n)] 
print(x) 

#67

import numpy as np 

arr = range(20) 
np.array_split(arr, 5)

#68

from itertools import islice 


def chunk(arr_range, arr_size): 
	arr_range = iter(arr_range) 
	return iter(lambda: tuple(islice(arr_range, arr_size)), ()) 


list(chunk(range(30), 5)) 

#69

from collections import deque 

def split_list(input_list, chunk_size): 
# Create a deque object from the input list 

deque_obj = deque(input_list) 
# While the deque object is not empty 
while deque_obj: 
	# Pop chunk_size elements from the left side of the deque object 
	# and append them to the chunk list 
	chunk = [] 
	for _ in range(chunk_size): 
		if deque_obj: 
		chunk.append(deque_obj.popleft()) 
		
	# Yield the chunk 
	yield chunk 
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
chunk_size = 3
chunks = list(split_list(input_list, chunk_size)) 
print(chunks) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]] 

#70

my_list = list(range(10)) 
chunk_size = 3
while my_list: 
	chunk, my_list = my_list[:chunk_size], my_list[chunk_size:] 
	print(chunk)

#71

# to sort one list using
# the other list


def sort_list(list1, list2):

	zipped_pairs = zip(list2, list1)

	z = [x for _, x in sorted(zipped_pairs)]

	return z


# driver code
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 3]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 3]

print(sort_list(x, y))

#72

def sorting_of_element(list1, list2):

	# initializing blank dictionary
	f_1 = {}

	# initializing blank list
	final_list = []

	# Addition of two list in one dictionary
	f_1 = {list1[i]: list2[i] for i in range(len(list2))}

	# sorting of dictionary based on value
	f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

	# Element addition in the list
	for i in f_lst.keys():
		final_list.append(i)
	return final_list


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]


list3 = sorting_of_element(list1, list2)
print(list3)

#73

# to sort values of first list based on second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
a = list(set(list2))
a.sort()
res = []
for i in a:
	for j in range(0, len(list2)):
		if(list2[j] == i):
			res.append(list1[j])
print(res)

#74

# to sort values of first list based on second list
from collections import OrderedDict
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
d = OrderedDict(zip(list1, list2))
res = list(OrderedDict(sorted(d.items(), key=lambda x: x[1])))
print(res)

#75

import numpy as np

# Define a function that takes two lists as input, sorts the first list based on
# the order of the second list, and returns the sorted list as a numpy array
def sort_list(list1, list2):
	# Use numpy's argsort function to get the indices that would sort the second list
	idx = np.argsort(list2)
	# Index the first list using the sorted indices and return the result as a numpy array
	return np.array(list1)[idx]

# Define two lists of strings and integers to be used as inputs for the sort_list function
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

# Call the sort_list function with the two lists and print the result
print(sort_list(x, y))

# Define another two lists of strings and integers to be used as inputs for the sort_list function
x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

# Call the sort_list function with the two lists and print the result
print(sort_list(x, y))

