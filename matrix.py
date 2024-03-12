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
			