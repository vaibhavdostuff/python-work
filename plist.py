#1
list1 = [2, 7, 5, 64, 14]
for a, i in enumerate(list1):
	if i % 2 == 0:
		print(i, end=" ")

#2
list1 = [2, 7, 5, 64, 14]
for i in list1:
	if (i % 2 != 0):
		pass
	else:
		print(i, end=" ")


#3
# Python code To print all even numbers
# in a given list using numpy array
import numpy as np

# Declaring Range
temp = [2, 7, 5, 64, 14]
li = np.array(temp)

# printing even numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)

#4
		