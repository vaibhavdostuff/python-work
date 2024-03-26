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
# Python3 code to demonstrate working of
# Extract Unique values dictionary values
import operator as op
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
	if op.countOf(res,i)==0:
		res.append(i)
res.sort()

# printing result
print("The unique values list is : " + str(res))

#6
#Python3 code to demonstrate working of
#Extract Unique values dictionary values
#initializing dictionary
test_dict = {'a' : [5, 6, 7, 8],
'b' : [10, 11, 7, 5],
'c' : [6, 12, 10, 8],
'd' : [1, 2, 5]}

#printing original dictionary
print("The original dictionary is : " + str(test_dict))

#Extract Unique values dictionary values
result = list(set(sum(test_dict.values(), [])))

#printing result
print("The unique values list is : " + str(result))

#7
# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#8
# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):

	sum = 0
	for i in dict.values():
		sum = sum + i

	return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#9
# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):

	sum = 0
	for i in dict:
		sum = sum + dict[i]

	return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#10
# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):
	return sum(dict.values())


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#11
import functools

dic = {'a': 100, 'b': 200, 'c': 300}

sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 0)

print("Sum :", sum_dic)

#12
import functools

def sum_dict_values(dict):
	return functools.reduce(lambda acc, x: acc + dict[x], dict, 0)

# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", sum_dict_values(dict))

#13
# Initializing dictionary
test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Mani
del test_dict['Mani']

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)

# Using del to remove a dict
# raises exception
del test_dict['Mani']

#14
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : " + str(test_dict))

# Using pop() to remove a dict. pair
# removes Mani
removed_value = test_dict.pop('Mani')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

print('\r')

# Using pop() to remove a dict. pair
# doesn't raise exception
# assigns 'No Key found' to removed_value
removed_value = test_dict.pop('Manjeet', 'No Key found')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

#15
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, 
			"Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing\
remove is : " + str(test_dict))

# Using items() + dict comprehension to remove a dict. pair
# removes Mani
new_dict = {key: val for key, 
			val in test_dict.items() if key != 'Mani'}

# Printing dictionary after removal
print("The dictionary after remove is : " + str(new_dict))

#16
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : \n" + str(test_dict))

a_dict = {key: test_dict[key] for key in test_dict if key != 'Mani'}

print("The dictionary after performing remove is : \n", a_dict)

#17
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
y = {}
# eliminate the unrequired element
for key, value in test_dict.items():
	if key != 'Arushi':
		y[key] = value
print(y)

#18
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
del test_dict
try:
	print(test_dict)
except:
	print('Deleted!')

#19
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
test_dict.clear()
print("Length", len(test_dict))
print(test_dict)

#20
# Python code demonstrate the working of sorted() and itemgetter

# importing "operator" for implementing itemgetter
from operator import itemgetter

# Initializing list of dictionaries
my_list = [{"name": "Nandini", "age": 20},
           {"name": "Manjeet", "age": 20},
           {"name": "Nikhil", "age": 19}]

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ")
print(sorted(my_list, key=itemgetter('age')))

print("\r")

# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(my_list, key=itemgetter('age', 'name')))

print("\r")

# using sorted and itemgetter to print list
# sorted by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(my_list, key=itemgetter('age'), reverse=True))

#21
# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
	{"name": "Manjeet", "age": 20},
	{"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))

print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))

#22
# Python code to merge dict using update() method
def Merge(dict1, dict2):
	return(dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)

#23
# Python code to merge dict using a single 
# expression
def Merge(dict1, dict2):
	res = {**dict1, **dict2}
	return res
	
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#24
from collections import ChainMap

# create the dictionaries to be merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# create a ChainMap with the dictionaries as elements
merged_dict = ChainMap(dict1, dict2)

# access and modify elements in the merged dictionary
print(merged_dict['a']) # prints 1
print(merged_dict['c']) # prints 3
merged_dict['c'] = 5 # updates value in dict2
print(merged_dict['c']) # prints 5

# add a new key-value pair to the merged dictionary
merged_dict['e'] = 6 # updates dict1
print(merged_dict['e']) # prints 6

#25
def merge_dictionaries(dict1, dict2):
	merged_dict = dict1.copy()
	merged_dict.update(dict2)
	return merged_dict

# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}

print(merge_dictionaries(dict1, dict2))

#26
# method to merge two dictionaries using the dict() constructor with the union operator (|)
def Merge(dict1, dict2):
	# create a new dictionary by merging the items of the two dictionaries using the union operator (|)
	merged_dict = dict(dict1.items() | dict2.items())
	# return the merged dictionary
	return merged_dict

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# merge the two dictionaries using the Merge() function
merged_dict = Merge(dict1, dict2)

# print the merged dictionary
print(merged_dict)

#27
# Python3 code to demonstrate working of 
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product

# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))

# printing result 
print("Flattened dictionary : " + str(res)) 

#28
# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict()
for i in range(0,len(a)):
	d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))

#29
test_dict = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
res = {test_dict['month'][i]: test_dict['name'][i] for i in range(len(test_dict['month']))}
print("Flattened dictionary:", res)

#30
