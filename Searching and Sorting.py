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
def insertion_sort_recursive(arr):
	# base case: return when array has only one element
	if len(arr) <= 1:
		return arr

	# recursively sort the first half of the array
	mid = len(arr) // 2
	left_half = insertion_sort_recursive(arr[:mid])

	# recursively sort the second half of the array
	right_half = insertion_sort_recursive(arr[mid:])

	# merge the sorted halves into a sorted array
	i, j = 0, 0
	sorted_arr = []
	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			sorted_arr.append(left_half[i])
			i += 1
		else:
			sorted_arr.append(right_half[j])
			j += 1
	sorted_arr += left_half[i:]
	sorted_arr += right_half[j:]

	return sorted_arr
arr = [5, 2, 4, 6, 1, 3]
sorted_arr = insertion_sort_recursive(arr)
print(sorted_arr) # Output: [1, 2, 3, 4, 5, 6]

#9
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort

def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

#10
# Approach 2: Quicksort using list comprehension

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

#11
# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

#12
# Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    # Traverse through all array elements
    for i in range(n-1):

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        swapped = False
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

#13
def bubblesort(elements):
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        swapped = False
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return

elements = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)

#14
from collections import Counter

def counting_sort(arr):
	count = Counter(arr)
	output = []
	for c in sorted(count.keys()):
		output +=  * count
	return output

arr = "geeksforgeeks"
arr = list(arr)
arr = counting_sort(arr)
output = ''.join(arr)
print("Sorted character array is", output)

#15
# Python program for implementation of Shell Sort

def shellSort(arr):

	# Start with a big gap, then reduce the gap
	n = len(arr)
	gap = n/2

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:

		for i in range(gap,n):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap /= 2


# Driver code to test above
arr = [ 12, 34, 54, 2, 3]

n = len(arr)
print ("Array before sorting:")
for i in range(n):
	print(arr[i]),

shellSort(arr)

print ("\nArray after sorting:")
for i in range(n):
	print(arr[i]),

#16
#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list) #dictionary containing adjacency List
		self.V = vertices #No. of vertices

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# neighbors generator given key
	def neighbor_gen(self,v):
		for k in self.graph[v]:
			yield k
	
	# non recursive topological sort
	def nonRecursiveTopologicalSortUtil(self, v, visited,stack):
		
		# working stack contains key and the corresponding current generator
		working_stack = [(v,self.neighbor_gen(v))]
		
		while working_stack:
			# get last element from stack
			v, gen = working_stack.pop()
			visited[v] = True
			
			# run through neighbor generator until it's empty
			for next_neighbor in gen:
				if not visited[next_neighbor]: # not seen before?
					# remember current work
					working_stack.append((v,gen))
					# restart with new neighbor
					working_stack.append((next_neighbor, self.neighbor_gen(next_neighbor)))
					break
			else:
				# no already-visited neighbor (or no more of them)
				stack.append(v)
				
	# The function to do Topological Sort.
	def nonRecursiveTopologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		
		# result stack
		stack = []

		# Call the helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if not(visited[i]):
				self.nonRecursiveTopologicalSortUtil(i, visited,stack)
		# Print contents of the stack in reverse
		stack.reverse()
		print(stack)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("The following is a Topological Sort of the given graph")
g.nonRecursiveTopologicalSort()

#17
import bisect

def binary_search(arr, val, start, end):
	idx = bisect.bisect_left(arr[start:end+1], val)
	return start + idx

def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

print("Sorted array:")
print(insertion_sort([37, 23, 0, 17, 12, 72, 31,
					46, 100, 88, 54]))

#18
# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/


def compAndSwap(a, i, j, dire):
	if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] > a[j]):
		a[i], a[j] = a[j], a[i]

# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.


def bitonicMerge(a, low, cnt, dire):
	if cnt > 1:
		k = cnt//2
		for i in range(low, low+k):
			compAndSwap(a, i, i+k, dire)
		bitonicMerge(a, low, k, dire)
		bitonicMerge(a, low+k, k, dire)

# This function first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order


def bitonicSort(a, low, cnt, dire):
	if cnt > 1:
		k = cnt//2
		bitonicSort(a, low, k, 1)
		bitonicSort(a, low+k, k, 0)
		bitonicMerge(a, low, cnt, dire)

# Caller of bitonicSort for sorting the entire array of length N
# in ASCENDING order


def sort(a, N, up):
	bitonicSort(a, 0, N, up)


# Driver code to test above
a = [3, 7, 4, 8, 6, 2, 1, 5]
n = len(a)
up = 1

sort(a, n, up)
print("Sorted array is")
for i in range(n):
	print("%d" % a[i], end=" ")

#19
