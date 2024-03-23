#1
# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()

# initializing dictionary
test_dict = {'a': [5, 6, 7, 8],
			'b': [10, 11, 7, 5],
			'c': [6, 12, 10, 8],
			'd': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))

# printing result
print("The unique values list is : " + str(res))

#2
# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using chain() + sorted() + values()
from itertools import chain

# initializing dictionary
test_dict = {'a': [5, 6, 7, 8],
			'b': [10, 11, 7, 5],
			'c': [6, 12, 10, 8],
			'd': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using chain() + sorted() + values()
res = list(sorted(set(chain(*test_dict.values()))))

# printing result
print("The unique values list is : " + str(res))

#3
# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# initializing dictionary
test_dict = {'a' : [5, 6, 7, 8],
			'b' : [10, 11, 7, 5],
			'c' : [6, 12, 10, 8],
			'd' : [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

x=list(test_dict.values())
y=[]
res=[]
for i in x:
	y.extend(i)
for i in y:
	if i not in res:
		res.append(i)
res.sort()

# printing result
print("The unique values list is : " + str(res))

#4
# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# initializing dictionary
from collections import Counter
test_dict = {'a': [5, 6, 7, 8],
			'b': [10, 11, 7, 5],
			'c': [6, 12, 10, 8],
			'd': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

valuesList = []
for key, values in test_dict.items():
	for value in values:
		valuesList.append(value)
freq = Counter(valuesList)
uniqueValues = list(freq.keys())
uniqueValues.sort()

# printing result
print("The unique values list is : " + str(uniqueValues))

#5
