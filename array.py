#1
# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)


# main function
if __name__ == "__main__":
	# input values to list
	arr = [12, 3, 4, 15]

	# calculating length of array
	n = len(arr)
	# calling function ans store the sum in ans
	ans = _sum(arr)
	# display sum
	print('Sum of the array is ', ans)
	
#2
# Python 3 code to find sum
# of elements in given array

# input values to list
arr = [12, 3, 4, 15]

# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)

# display sum
print('Sum of the array is ', ans)

#3
from functools import reduce
# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# iterate over array
	# using reduce and get 
	# sum on accumulator
	sum = reduce(lambda a, b: a+b, arr) 

	return(sum)


# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print('Sum of the array is ', ans)

#4
list1 = [12, 3, 4, 15];
s = 0
for i,a in enumerate(list1): 
 s+=a # i have to see to it
print(s)

#5
def sum_of_array(arr, low, high):
	if low == high:
		return arr[low]
	mid = (low + high) // 2
	left_sum = sum_of_array(arr, low, mid)
	right_sum = sum_of_array(arr, mid+1, high)
	return left_sum + right_sum
#Examples
arr = [1, 2, 3]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 6

arr = [15, 12, 13, 10]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 50

#6
from collections import Counter

arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0

for key, value in c.items():
	sum += key * value

print("Sum of the array is", sum)

#7
# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

#8
# Python3 program to find maximum
# in arr[] of size n
def largest(arr, n):
	ans = max(arr)
	return ans;

# Driver code
if __name__ == '__main__':
	arr = [10, 324, 45, 90, 9808]
	n = len(arr)
	print ("Largest in given array ", largest(arr, n))

#9
# Python3 program to find maximum
# in arr[] of size n
from functools import reduce


def largest(arr):

	# Sort the array
	ans = reduce(max, arr)

	return ans
	# or returning largest value


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array ", Ans)

#10
# python program to find large number in the given array
import operator
# Initializing the list
arr = [2, 1, 7, 3, 0]
max=0

# printing the original list
print('The given array is:', arr)

#checking for large element
for i in arr:
	if operator.gt(i,max):
		max=i

# printing the large number in the array
print('The biggest number in the given array is:', max)

#11
array = [10, 5, 20, 8, 15]

largest_element = max(array, key=lambda x: x)
print("Largest element in the array:", largest_element)

#12
# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
