#1
# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
	
#2
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

#3
import bisect

def binary_search_bisect(arr, x):
	i = bisect.bisect_left(arr, x)
	if i != len(arr) and arr[i] == x:
		return i
	else:
		return -1
	
# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search_bisect(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

#4
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

#5
# This is similar to the above one, with the only difference 
# being that it is using the recursive approach instead of iterative.


def search(arr, curr_index, key):
	if curr_index == -1:
		return -1
	if arr[curr_index] == key:
		return curr_index
	return search(arr, curr_index-1, key)

#6
import re

# Sample input
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110

# Convert the array to a string
arr_str = ','.join(str(i) for i in arr)

# Use regular expression to search for the element in the string
match = re.search(r'\b{}\b'.format(x), arr_str)

# Output
if match:
	# Calculate the index by counting the number of commas before the match
	result = arr_str[:match.start()].count(',')
	print(f"Element {x} is present at index {result}")
else:
	print(f"Element {x} is not present in the array")

#7
def insertionSort(arr):
	n = len(arr) # Get the length of the array
	
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

#8
