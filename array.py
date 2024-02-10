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
list1 = [12, 3, 4, 15];s=0
for i,a in enumerate(list1): 
s+=a 
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

