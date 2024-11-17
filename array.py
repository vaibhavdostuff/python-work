#1
# to find sum of elements in given array

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

	arr = [12, 3, 4, 15]

	n = len(arr)
	# calling function ans store the sum in ans
	ans = _sum(arr)
	# display sum
	print('Sum of the array is ', ans)
	
#2

arr = [12, 3, 4, 15]

# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)

# display sum
print('Sum of the array is ', ans)

#3

from functools import reduce

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

arr = [22, 30, 14, 5]
c = Counter(arr)
sum = 0

for key, value in c.items():
	sum += key * value

print("Sum of the array is", sum)

#7

# to find maximum in arr[] of size n

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
arr = [10, 324, 45, 90, 988]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

#8


def largest(arr, n):
	ans = max(arr)
	return ans;

# Driver code
if __name__ == '__main__':
	arr = [34, 24, 4, 63, 908]
	n = len(arr)
	print ("Largest in given array ", largest(arr, n))

#9

from functools import reduce


def largest(arr):

	# Sort the array
	ans = reduce(max, arr)

	return ans
	# or returning largest value


# Driver Code
arr = [101, 324, 65, 90, 808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array ", Ans)

#10

# to find large number in the given array
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

#13

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
	for i in range(gcd(d, n)):

		# move i-th values of blocks
		temp = arr[i]
		j = i
		while 1:
			k = j + d
			if k >= n:
				k = k - n
			if k == i:
				break
			arr[j] = arr[k]
			j = k
		arr[j] = temp

# UTILITY FUNCTIONS
# function to print an array


def printArray(arr, size):
	for i in range(size):
		print("%d" % arr[i], end=" ")

# Function to get gcd of a and b


def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

#14

# Function to reverse arr[]
def rverseArray(arr,d):
	c=(arr[d:])+(arr[:d])
	return c
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
d=2
print(rverseArray(arr,d))

#15

# for reversal algorithm of array rotation

# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
	while (start < end):
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end = end-1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
	n = len(arr)
	rverseArray(arr, 0, d-1)
	rverseArray(arr, d, n-1)
	rverseArray(arr, 0, n-1)
# Function to print an array
def printArray(arr):
	for i in range(0, len(arr)):
		print (arr[i])
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)

#16

# to split array and move first
# part to end.


def splitArr(a, n, k):
	b = a[:k]
	return (a[k::]+b[::])


# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
	print(arr[i], end=' ')

#17

arr = [10, 20, 15, 60, 12, 46]
n = len(arr)
position = 2
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
	print(i, end=" ")

#18

def split_and_add(arr, n):
	return [arr[(i + n) % len(arr)] for i in range(len(arr))]


arr = [12, 10, 5, 6, 52, 36]
n = 2

result = split_and_add(arr, n)

print(*result)

#19

# This code finds the remainder of the product of all the elements in the array arr divided by 'n'.
def findremainder(arr, len, n):
	product = 1
	for i in range(len):
		product = product * arr[i]
	return product % n


arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))

#20

from functools import reduce

def remainderAfterMultiplication(arr, n):
	result = reduce(lambda x, y: (x * y) % n, arr)
	return result

# Driver Code
arr1 = [100, 10, 5, 25, 35, 14]
n1 = 11
result1 = remainderAfterMultiplication(arr1, n1)
print(result1)

arr2 = [100, 10]
n2 = 5
result2 = remainderAfterMultiplication(arr2, n2)
print(result2)

#21

# Check if given array is Monotonic
def isMonotonic(A):
	x, y = [], []
	x.extend(A)
	y.extend(A)
	x.sort()
	y.sort(reverse=True)
	if(x == A or y == A):
		return True
	return False


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))

#22

def isMonotonic(arr):
	if len(arr) <= 2:
		return True
	direction = arr[1] - arr[0]
	for i in range(2, len(arr)):
		if direction == 0:
			direction = arr[i] - arr[i - 1]
			continue
		if (direction > 0 and arr[i] < arr[i - 1]) or (direction < 0 and arr[i] > arr[i - 1]):
			return False
	return True

# Example usage
arr1 = [1, 2, 3, 4, 5] # True
arr2 = [5, 4, 3, 2, 1] # True
arr3 = [1, 3, 3, 5, 4] # True
arr4 = [4, 2, 3, 4, 1, 4] # False

print(isMonotonic(arr1)) # should return True
print(isMonotonic(arr2)) # should return True
print(isMonotonic(arr3)) # should return True
print(isMonotonic(arr4)) # should return False
