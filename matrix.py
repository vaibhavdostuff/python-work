#1
# Program to add two matrices using nested loop

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)): 
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)

#2
# Program to add two matrices
# using list comprehension

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

result = [[X[i][j] + Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

for r in result:
	print(r)

#3
# Program to add two matrices
# using zip()

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

result = [map(sum, zip(*t)) for t in zip(X, Y)]

print(result)

#4
# Program to add two matrices
# using numpy

import numpy as np

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]

result = np.array(X) + np.array(Y)

print(result)

#5
from sympy import Matrix

X = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]

Y = [[9, 8, 7],
	[6, 5, 4],
	[3, 2, 1]]

# Create Matrix objects from the lists
matrix_x = Matrix(X)
matrix_y = Matrix(Y)

# Add the matrices
result = matrix_x + matrix_y

# Print the result
print(result)

#6
# Program to multiply two matrices using list comprehension

# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col)) 
						for B_col in zip(*B)]
								for A_row in A]

for r in result:
	print(r)

#7
# Program to multiply two matrices (vectorized implementation)

# Program to multiply two matrices (vectorized implementation)
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4

result= [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]

result = np.dot(A,B)

for r in result:
	print(r)

#8
def matrix_multiply_recursive(A, B):
	# check if matrices can be multiplied
	if len(A[0]) != len(B):
		raise ValueError("Invalid matrix dimensions")

	# initialize result matrix with zeros
	result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

	# recursive multiplication of matrices
	def multiply(A, B, result, i, j, k):
		if i >= len(A):
			return
		if j >= len(B[0]):
			return multiply(A, B, result, i+1, 0, 0)
		if k >= len(B):
			return multiply(A, B, result, i, j+1, 0)
		result[i][j] += A[i][k] * B[k][j]
		multiply(A, B, result, i, j, k+1)

	# perform matrix multiplication
	multiply(A, B, result, 0, 0, 0)
	return result


# example usage
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

result = matrix_multiply_recursive(A, B)
for row in result:
	print(row)

#9
# Python3 code to demonstrate
# Matrix Product
# Using list comprehension + loop

# getting Product


def prod(val):
	res = 1
	for ele in val:
		res *= ele
	return res


# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + loop
# Matrix Product
res = prod([ele for sub in test_list for ele in sub])

# print result
print("The total element product in lists is : " + str(res))

#10
# Python3 code to demonstrate
# Matrix Product
# Using chain() + loop
from itertools import chain

# getting Product


def prod(val):
	res = 1
	for ele in val:
		res *= ele
	return res


# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using chain() + loop
# Matrix Product
res = prod(list(chain(*test_list)))

# print result
print("The total element product in lists is : " + str(res))

#11
# Python3 code to demonstrate
# Matrix Product

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

x = []
for i in test_list:
	x.extend(i)
res = 1
for j in x:
	res *= j


# print result
print("The total element product in lists is : " + str(res))

#12
# Python3 code to demonstrate
# Matrix Product

# initializing list
import operator
from functools import reduce
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

x = []
for i in test_list:
	x.extend(i)

res = reduce(operator.mul, x, 1)

# print result
print("The total element product in lists is : " + str(res))

#13
# Python3 code to demonstrate
# Matrix Product

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))
res = 1
for i in test_list:
	for j in i:
		res *= j

# print result
print("The total element product in lists is : " + str(res))

#14
# function to calculate the product of all elements in the nested list
def multiply_nested_list(nested_list):
	res = 1
	for i in nested_list:
		if isinstance(i, list):
			res *= multiply_nested_list(i)
		else:
			res *= i
	return res

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# call the function to get the product
res = multiply_nested_list(test_list)

# print result
print("The total element product in lists is : " + str(res))

#15
# importing numpy as np
import numpy as np


# creating first matrix
A = np.array([[1, 2], [3, 4]])

# creating second matrix
B = np.array([[4, 5], [6, 7]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))

#16
# importing numpy as np
import numpy as np


# creating first matrix
A = np.array([[1, 2], [3, 4]])

# creating second matrix
B = np.array([[4, 5], [6, 7]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

# subtracting two matrix
print("Subtraction of two matrix")
print(np.subtract(A, B))

#17
# Input matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]

# Printing elements of matrix1
print("Printing elements of first matrix")
for row in matrix1:
	for element in row:
		print(element, end=" ")
	print()

# Printing elements of matrix2
print("Printing elements of second matrix")
for row in matrix2:
	for element in row:
		print(element, end=" ")
	print()

# Subtracting two matrices
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
	for j in range(len(matrix1[0])):
		result[i][j] = matrix1[i][j] - matrix2[i][j]

# Printing the result
print("Subtraction of two matrix")
for row in result:
	for element in row:
		print(element, end=" ")
	print()

#18
m = [[1, 2], [3, 4], [5, 6]]
for row in m:
	print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
	print(row)

#19
matrix = [(1, 2, 3), (4, 5, 6), 
				(7, 8, 9), (10, 11, 12)]
for row in matrix:
	print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
	print(row)

#20
import numpy
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))

#21
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print("\n")
print(matrix.T)

#22
from itertools import chain
import time
import numpy as np

def transpose2(M):
	n = len(M[0])
	L = list(chain(*M))
	return [L[i::n] for i in range(n)]

start = time.time_ns()
matrix = np.array([[1, 2, 3], [4, 5, 6]])
end = time.time_ns()
print(transpose2(matrix))
print("Time taken", end-start, "ns")

#23
# Python3 code to demonstrate
# matrix creation of n * n
# using list comprehension

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# using list comprehension
# matrix creation of n * n
res = [list(range(1 + N * i, 1 + N * (i + 1)))
							for i in range(N)]

# print result
print("The created matrix of N * N: " + str(res))

#24
# Python3 code to demonstrate
# matrix creation of n * n
# using next() + itertools.count()
import itertools

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# using next() + itertools.count()
# matrix creation of n * n
temp = itertools.count(1) 
res = [[next(temp) for i in range(N)] for i in range(N)]

# print result
print("The created matrix of N * N: " + str(res))

#25
# Python3 code to demonstrate
# matrix creation of n * n

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# using list comprehension
# matrix creation of n * n
x=N*N
y=[]
for i in range(1,x+1):
	y.append(i)
res=[]
i=0
while(i<len(y)):
	a=y[i:i+N]
	res.append(a)
	i+=N
# print result
print("The created matrix of N * N: " + str(res))

#26
# Python3 code to demonstrate working of
# Get Kth Column of Matrix
# using list comprehension

# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Get Kth Column of Matrix
# using list comprehension
res = [sub[K] for sub in test_list]

# printing result
print("The Kth column of matrix is : " + str(res))

#27
# Python code to demonstrate working of
# Get Kth Column of Matrix
# using zip()

# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Get Kth Column of Matrix
# using zip()
res = list(zip(*test_list)[K])

# printing result
print("The Kth column of matrix is : " + str(res))

#28
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

K = 2

res = []

for i in range(len(test_list)):
	res.append(test_list[i][K])

print("The Kth column of matrix is : " + str(res))

#29
	