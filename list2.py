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
my_list = [4, 5, 6, 7, 8, 9]

# Convert the list to a 1D numpy array
my_array = np.array(my_list)

# Reverse the order of the array
reversed_array = my_array[::-1]

# Convert the reversed array to a list
reversed_list = reversed_array.tolist()

# Print the reversed list
print(reversed_list)

#7
# Python program to find sum of elements in list

total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)

#8
# Python program to find sum of elements in list
total = 0
ele = 0

# creating a list
list1 = [11, 5, 17, 18, 23] 

# Iterate each element in list
# and add them in variable total
while(ele < len(list1)):
	total = total + list1[ele]
	ele += 1
	
# printing total value
print("Sum of all elements in given list: ", total)

#9
# Python program to find sum of all
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
# Python program to find sum of elements in list

# creating a list
list1 = [11, 5, 17, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print("Sum of all elements in given list: ", total)

#11
# Python 3 program to find the sum of all elements in the
# list using add function of operator module

from operator import*
list1 = [12, 15, 3, 10]
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
list1 = [12, 15, 3, 10]
print(sum(list(filter(lambda x: (x),list1))))

#15
import operator
list1 = [12, 15, 3, 10] ;s=0
for i in list1:
s=s+operator.add(0,i)
print(s)

#16
# Python program to multiply all values in the
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
# Python3 program to multiply all values in the
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
# Python3 program to multiply all values in the
# list using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

#19
# Python3 program to multiply all values in the
# list using math.prod
import math
list1 = [1, 2, 3] 
list2 = [3, 2, 4]

result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)

#20
# Python 3 program to multiply all numbers in
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
# Python program to multiply all values in the
# list using traversal

def multiplyList(myList) :
	
	# Multiply elements one by one
	result = 1
	for i in range(0,len(myList)):
		result = result * myList[i]
	return result
	
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

#23
# Python3 program to multiply all values in the
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

list1 = [1, 2, 3]
result = reduce(mul, list1)

print(result)

#26
# Python program to find smallest 
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", list1[0])

#27
# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort(reverse=True)

# printing the first element
print("Smallest element is:", list1[-1])

#28
# Python program to find smallest 
# number in a list

# list of numbers
list1 = [10, 20, 1, 45, 99]


# printing the minimum element
print("Smallest element is:", min(list1))

#29
# Python program to find smallest 
# number in a list

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
# Python program to find smallest 
# number in a list

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
# Python code to print smallest element in the list

lst = [20, 10, 20, 1, 100]
print(min(lst, key=lambda value: int(value)) )

#32
lst = [20, 10, 20, 1, 100] 
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)

#33
# Python code to print smallest element in the list
from functools import reduce
lst = [20, 10, 20, 15, 100]
print(reduce(min,lst) )

#34
# defining the list
arr = [5,2,3,2,5,4,7,9,7,10,15,68]

# converting the list into set
set_arr = set(arr)

# Now using the min function to get the minimum
# value from the set

print(min(set_arr))

#35
arr = [2,6,8,4,9,7,52,3,6,2,4,5,6,8,2]

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
# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])

#37
# Python program to find largest
# number in a list

# List of numbers
list1 = [10, 20, 4, 45, 99]

# Printing the maximum element
print("Largest element is:", max(list1))

#38
# Python program to find largest
# number in a list


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
# python code to print largest element in the list

lst = [20, 10, 20, 4, 100]
print(max(lst, key=lambda value: int(value)) )

#40
from functools import reduce
lst = [20, 10, 20, 4, 100]
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
# Python program to find second largest
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
# Python program to find largest number
# in a list

# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])

#46
