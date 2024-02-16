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
