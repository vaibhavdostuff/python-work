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

