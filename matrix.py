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
	