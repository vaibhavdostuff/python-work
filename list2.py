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
