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
# Python3 code to demonstrate working of 
# Convert key-values list to flat dictionary
# Using for loop

# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using for loop
res = {}
for i in range(len(test_dict['month'])):
	res[test_dict['month'][i]] = test_dict['name'][i]

# printing result 
print("Flattened dictionary : " + str(res))

#31
# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

# Initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# Inserting items in starting of dict
iniordered_dict.update({'manjeet': '3'})
iniordered_dict.move_to_end('manjeet', last=False)

# Printing result
print("Resultant Dictionary : "+str(iniordered_dict))

#32
# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

# initialising ordered_dict
ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])

# adding in beginning of dict
both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))

# print result
print ("Resultant Dictionary :"+str(both))

#33
from collections import OrderedDict

# Initialising ordered_dict
ini_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# Creating a iniordered ordered dict
iniordered_dict = OrderedDict()

# Inserting new key-value pair at the beginning of iniordered_dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

# popitem() method to remove and insert key-value pair at beginning
while ini_dict:
	iniordered_dict.update({ini_dict.popitem(last=False)})

# Print result
print("Resultant Dictionary :" + str(iniordered_dict))

#34
# Function to check if string follows order of 
# characters defined by a pattern 
from collections import OrderedDict 

def checkOrder(input, pattern): 
	
	# create empty OrderedDict 
	# output will be like {'a': None,'b': None, 'c': None} 
	dict = OrderedDict.fromkeys(input) 

	# traverse generated OrderedDict parallel with 
	# pattern string to check if order of characters 
	# are same or not 
	ptrlen = 0
	for key,value in dict.items(): 
		if (key == pattern[ptrlen]): 
			ptrlen = ptrlen + 1
		
		# check if we have traverse complete 
		# pattern string 
		if (ptrlen == (len(pattern))): 
			return 'true'

	# if we come out from for loop that means 
	# order was mismatched 
	return 'false'

# Driver program 
if __name__ == "__main__": 
	input = 'engineers rock'
	pattern = 'er'
	print (checkOrder(input,pattern)) 

#35
def check_order(string, pattern):
	i, j = 0, 0
	for char in string:
		if char == pattern[j]:
			j += 1
		if j == len(pattern):
			return True
		i += 1

	return False
string = 'engineers rock'
pattern = 'er'
print(check_order(string, pattern))

#36
# Function to find winner of an election where votes 
# are represented as candidate names 
from collections import Counter 

def winner(input): 

	# convert list of candidates into dictionary 
	# output will be likes candidates = {'A':2, 'B':4} 
	votes = Counter(input) 
	
	# create another dictionary and it's key will 
	# be count of votes values will be name of 
	# candidates 
	dict = {} 

	for value in votes.values(): 

		# initialize empty list to each key to 
		# insert candidate names having same 
		# number of votes 
		dict[value] = [] 

	for (key,value) in votes.items(): 
		dict[value].append(key) 

	# sort keys in descending order to get maximum 
	# value of votes 
	maxVote = sorted(dict.keys(),reverse=True)[0] 

	# check if more than 1 candidates have same 
	# number of votes. If yes, then sort the list 
	# first and print first element 
	if len(dict[maxVote])>1: 
		print (sorted(dict[maxVote])[0])
	else: 
		print (dict[maxVote][0]) 

# Driver program 
if __name__ == "__main__": 
	input =['john','johnny','jackie','johnny',
			'john','jackie','jamie','jamie',
			'john','johnny','jamie','johnny',
			'john'] 
	winner(input) 

#37
from collections import Counter 

votes =['john','johnny','jackie','johnny','john','jackie',
	'jamie','jamie','john','johnny','jamie','johnny','john'] 

#Count the votes for persons and stores in the dictionary
vote_count=Counter(votes)

#Find the maximum number of votes
max_votes=max(vote_count.values())

#Search for people having maximum votes and store in a list
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]

#Sort the list and print lexicographical smallest name
print(sorted(lst)[0])

#38
# Python3 code to demonstrate working of 
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using values() + keys() + list()

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# + operator is used to perform adding keys and values
res = list(test_dict.keys()) + list(test_dict.values())

# printing result 
print("The ordered keys and values : " + str(res)) 

#39
# Python3 code to demonstrate working of 
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using chain() + keys() + values()
from itertools import chain

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# chain() is used for concatenation
res = list(chain(test_dict.keys(), test_dict.values()))

# printing result 
print("The ordered keys and values : " + str(res)) 

#40
# Python3 code to demonstrate working of
# Append Dictionary Keys and Values 
#( In order ) in dictionary
# Using values() + keys() + extend()+list()

# initializing dictionary
test_dict = {"Gfg": 1, "is": 3, "Best": 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

a = list(test_dict.keys())
b = list(test_dict.values())
a.extend(b)
res = a

# printing result
print("The ordered keys and values : " + str(res))

#41
# initializing dictionary
test_dict = {"Gfg": 1, "is": 3, "Best": 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using the zip() function and list comprehension to append dictionary keys and values
res = [val for val in zip(test_dict.values(), test_dict.keys())]

# printing result
print("The ordered keys and values : " + str(res))

#42
# Python3 code to demonstrate working of 
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using sorted() + list comprehension

# initializing dictionary
test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using sorted() to get the keys in alphabetical order
keys = sorted(test_dict.keys())

# using list comprehension to get the values corresponding to each key
values = [test_dict[key] for key in keys]

# concatenating the keys and values lists
res = keys + values

# printing result 
print("The ordered keys and values : " + str(res)) 

#43
myDict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)

#44
# Function calling
def dictionary():
	# Declare hash function
	key_value = {}

# Initializing value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323

	print("Task 1:-\n")

	print("key_value", key_value)

	# iterkeys() returns an iterator over the
	# dictionary’s keys.
	for i in sorted(key_value.keys()):
		print(i, end=" ")


def main():
	# function calling
	dictionary()


# Main function calling
if __name__ == "__main__":
	main()

#45
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9',
		'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

#46
# function calling
def dictionairy():

	# Declaring the hash function
	key_value = {}

# Initialize value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	
	print("key_value",key_value)

	print("Task 2:-\nKeys and Values sorted in",
		"alphabetical order by the key ")
	

	# sorted(key_value) returns a sorted list
	# of the Dictionary’s keys.
	for i in sorted(key_value):
		print((i, key_value[i]), end=" ")


def main():
		# function calling
	dictionairy()


# main function calling
if __name__ == "__main__":
	main()

#47
# Function calling
def dictionairy():

	# Declaring hash function
	key_value = {}

# Initializing the value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	
	print("key_value",key_value)

	print("Task 3:-\nKeys and Values sorted",
		"in alphabetical order by the value")

	# Note that it will sort in lexicographical order
	# For mathematical way, change it to float
	print(sorted(key_value.items(), key=lambda kv: 
				(kv[1], kv[0])))


def main():
	# function calling
	dictionairy()


# main function calling
if __name__ == "__main__":
	main()

#48
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np

dict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)

#49
# Python3 code to demonstrate working of 
# Sort Dictionary key and values List
# Using loop + dictionary comprehension

# initializing dictionary
test_dict = {'gfg': [7, 6, 3], 
			'is': [2, 10, 3], 
			'best': [19, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using loop + dictionary comprehension
res = dict()
for key in sorted(test_dict):
	res[key] = sorted(test_dict[key])

# printing result 
print("The sorted dictionary : " + str(res)) 

#50
# Python3 code to demonstrate working of 
# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()

# initializing dictionary
test_dict = {'gfg': [7, 6, 3], 
			'is': [2, 10, 3], 
			'best': [19, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()
res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}

# printing result 
print("The sorted dictionary : " + str(res)) 

#51
# Python3 code to demonstrate working of 
# Sort Dictionary key and values List
# Using lambda function with sorted()

# initializing dictionary
test_dict = {'gfg': [7, 6, 3], 
			'is': [2, 10, 3], 
			'best': [19, 4]}

# printing original dictionary
print("The original dictionary is: " + str(test_dict))

# Sort Dictionary key and values List
# Using lambda function with sorted()
res = dict(sorted(test_dict.items(), key=lambda x: x[0]))

for key in res:
	res[key] = sorted(res[key])

# printing result 
print("The sorted dictionary: " + str(res))

#52
# Python3 code to demonstrate working of 
# Sort Dictionary key and values List
# Using zip() function with sorted()

# initializing dictionary
test_dict = {'gfg': [7, 6, 3], 
			'is': [2, 10, 3], 
			'best': [19, 4]}

# printing original dictionary
print("The original dictionary is: " + str(test_dict))

# Sort Dictionary key and values List
# Using zip() function with sorted()
keys = list(test_dict.keys())
values = list(test_dict.values())
sorted_tuples = sorted(zip(keys, values), key=lambda x: x[0])
res = {k: sorted(v) for k, v in sorted_tuples}

# printing result 
print("The sorted dictionary: " + str(res))

#53
def sort_dict_recursive(test_dict):
	if not test_dict:
		return {}
	min_key = min(test_dict.keys())
	sorted_values = sorted(test_dict[min_key])
	rest_dict = {k: v for k, v in test_dict.items() if k != min_key}
	sorted_rest_dict = sort_dict_recursive(rest_dict)
	return {min_key: sorted_values, **sorted_rest_dict}

test_dict = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}
res = sort_dict_recursive(test_dict)
print("The original dictionary is: " + str(test_dict))
print("The sorted dictionary : " + str(res))

#54
# Python code to demonstrate Dictionary and
# missing value error
d = { 'a' : 1 , 'b' : 2 }

# trying to output value of absent key 
print ("The value associated with 'c' is : ")
print (d['c'])

#55
ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
	print(ele["d"])
else:
	print("Key not found")

#56
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))

#57
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present') 

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])

#58
# Python code to demonstrate defaultdict
import collections

# declaring defaultdict
# sets default value 'Key Not found' to absent keys
defd = collections.defaultdict(lambda : 'Key Not found')

# initializing values 
defd['a'] = 1

# initializing values 
defd['b'] = 2

# printing value 
print ("The value associated with 'a' is : ",end="")
print (defd['a'])

# printing value associated with 'c'
print ("The value associated with 'c' is : ",end="")
print (defd['c'])

#59
country_code = {'India': '0091',
				'Australia': '0025',
				'Nepal': '00977'}

try:
	print(country_code['India'])
	print(country_code['USA'])
except KeyError:
	print('Not Found')

#60
# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;

# print the dictionary
print(dict)

#61
# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
		("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)

#62
# Creating a dictionary with multiple inputs for keys
data = {
	(1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
	(2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
	(3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
	(4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

# Accessing the values using the keys
print(data[(1, "John", "Doe")]["a"])
print(data[(2, "Jane", "Smith")]["f"])
print(data[(3, "Bob", "Johnson")]["j"])

data[(1, "John", "Doe")]["a"] = {"b": "marketing", "c": 75000};
data[(3, "Bob", "Johnson")]["j"] = {"h": 35, "i": "project"};
print(data[(1, "John", "Doe")]["a"]);
print(data[(3, "Bob", "Johnson")]["j"]);

#63
# Function to return all anagrams together
def allAnagram(input):
	
	# empty dictionary which holds subsets
	# of all anagrams together
	dict = {}

	# traverse list of strings
	for strVal in input:
		
		# sorted(iterable) method accepts any
		# iterable and returns list of items
		# in ascending order
		key = ''.join(sorted(strVal))
		
		# now check if key exist in dictionary
		# or not. If yes then simply append the
		# strVal into the list of it's corresponding
		# key. If not then map empty list onto
		# key and then start appending values
		if key in dict.keys():
			dict[key].append(strVal)
		else:
			dict[key] = []
			dict[key].append(strVal)

	# traverse dictionary and concatenate values
	# of keys together
	output = ""
	for key,value in dict.items():
		output = output + ' '.join(value) + ' '

	return output

# Driver function
if __name__ == "__main__":
	input=['cat', 'dog', 'tac', 'god', 'act']
	print (allAnagram(input))

#64
# Function to find k'th non repeating character
# in string
from collections import OrderedDict

def kthRepeating(input,k):

	# OrderedDict returns a dictionary data
		# structure having characters of input
	# string as keys in the same order they
		# were inserted and 0 as their default value
	dict=OrderedDict.fromkeys(input,0)

	# now traverse input string to calculate
		# frequency of each character
	for ch in input:
		dict[ch]+=1

	# now extract list of all keys whose value
		# is 1 from dict Ordered Dictionary
	nonRepeatDict = [key for (key,value) in dict.items() if value==1]
	
	# now return (k-1)th character from above list
	if len(nonRepeatDict) < k:
		return 'Less than k non-repeating characters in input.'
	else:
		return nonRepeatDict[k-1]

# Driver function
if __name__ == "__main__":
	input = "geeksforgeeks"
	k = 3
	print (kthRepeating(input, k))

#65
# function to Check if binary representations
# of two numbers are anagram
from collections import Counter

def checkAnagram(num1,num2):

	# convert numbers into in binary
	# and remove first two characters of 
	# output string because bin function 
	# '0b' as prefix in output string
	bin1 = bin(num1)[2:]
	bin2 = bin(num2)[2:]

	# append zeros in shorter string
	zeros = abs(len(bin1)-len(bin2))
	if (len(bin1)>len(bin2)):
		bin2 = zeros * '0' + bin2
	else:
		bin1 = zeros * '0' + bin1

	# convert binary representations 
	# into dictionary
	dict1 = Counter(bin1)
	dict2 = Counter(bin2)

	# compare both dictionaries
	if dict1 == dict2:
		print('Yes')
	else:
		print('No')

# Driver program
if __name__ == "__main__":
	num1 = 8
	num2 = 4
	checkAnagram(num1,num2)
	

#66
def is_anagram_binary(a, b):
	bin_a = bin(a)[2:].zfill(32)
	bin_b = bin(b)[2:].zfill(32)
	count_a = [0, 0]
	count_b = [0, 0]
	for i in range(32):
		if bin_a[i] == '0':
			count_a[0] += 1
		else:
			count_a[1] += 1
		if bin_b[i] == '0':
			count_b[0] += 1
		else:
			count_b[1] += 1
	if count_a == count_b:
		return "Yes"
	else:
		return "No"

a = 8
b = 4
print( is_anagram_binary(8, 4)) # Output: True

#67
# Function to find the size of largest subset 
# of anagram words
from collections import Counter

def maxAnagramSize(input):

	# split input string separated by space
	input = input.split(" ")

	# sort each string in given list of strings
	for i in range(0,len(input)):
		input[i]=''.join(sorted(input[i]))

	# now create dictionary using counter method
	# which will have strings as key and their 
	# frequencies as value
	freqDict = Counter(input)

	# get maximum value of frequency
	print (max(freqDict.values()))

# Driver program
if __name__ == "__main__":
	input = 'ant magenta magnate tan gnamate'
	maxAnagramSize(input)

#68
def largest_anagram_subset_size(words):
	anagram_dict = {}
	for word in words:
		sorted_word = ''.join(sorted(word))
		if sorted_word not in anagram_dict:
			anagram_dict[sorted_word] = []
		anagram_dict[sorted_word].append(word)
	max_count = max([len(val) for val in anagram_dict.values()])
	return max_count

words = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']
print(largest_anagram_subset_size(words)) 

#69
from collections import Counter

words = ['cars', 'bikes', 'arcs', 'steer']

max_anagrams = max(
	list(
		map(
			lambda x: sum(
				map(
					lambda y: Counter(y) == Counter(x), 
					words
				)
			),
			words
		)
	),
	default=0
)

print(max_anagrams)

#70
from collections import Counter

def remov_duplicates(input):

	# split input string separated by space
	input = input.split(" ")

	# now create dictionary using counter method
	# which will have strings as key and their 
	# frequencies as value
	UniqW = Counter(input)

	# joins two adjacent elements in iterable way
	s = " ".join(UniqW.keys())
	print (s)

# Driver program
if __name__ == "__main__":
	input = 'Python is great and Java is also great'
	remov_duplicates(input)

#71
# Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

	# If condition is used to store unique string 
	# in another list 'k' 
	if (s.count(i)>=1 and (i not in k)):
		k.append(i)
print(' '.join(k))

#72
# Python3 program

string = 'Python is great and Java is also great'

print(' '.join(dict.fromkeys(string.split())))

#73
string = 'Python is great and Java is also great'
print(' '.join(set(string.split())))

#74
# Program using operator.countOf()
import operator as op
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
# If condition is used to store unique string 
# in another list 'k' 
 if (op.countOf(l,i)>=1 and (i not in k)):
	 k.append(i)
print(' '.join(k))

#75
def remove_duplicates(sentence):
	words = sentence.split(" ")
	result = []
	for word in words:
		if word not in result:
			result.append(word)
	return " ".join(result)

sentence = "Python is great and Java is also great"
print(remove_duplicates(sentence))

#76
def remove_duplicates(sentence):
	words = sentence.split(" ")
	if len(words) == 1:
		return words[0]
	if words[0] in words[1:]:
		return remove_duplicates(" ".join(words[1:]))
	else:
		return words[0] + " " + remove_duplicates(" ".join(words[1:]))

sentence = "Python is great and Java is also great"
print(remove_duplicates(sentence))

#77
# function to mirror characters of a string

def mirrorChars(input,k):

	# create dictionary
	original = 'abcdefghijklmnopqrstuvwxyz'
	reverse = 'zyxwvutsrqponmlkjihgfedcba'
	dictChars = dict(zip(original,reverse))

	# separate out string after length k to change
	# characters in mirror
	prefix = input[0:k-1]
	suffix = input[k-1:]
	mirror = ''

	# change into mirror
	for i in range(0,len(suffix)):
		mirror = mirror + dictChars[suffix[i]]

	# concat prefix and mirrored part
	print (prefix+mirror)
		
# Driver program
if __name__ == "__main__":
	input = 'paradox'
	k = 3
	mirrorChars(input,k)

#78
def CountFrequency(my_list):

	# Creating an empty dictionary
	freq = {}
	for item in my_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print("% d : % d" % (key, value))


# Driver function
if __name__ == "__main__":
	my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

	CountFrequency(my_list)

#79
import operator


def CountFrequency(my_list):

	# Creating an empty dictionary
	freq = {}
	for items in my_list:
		freq[items] = my_list.count(items)

	for key, value in freq.items():
		print("% d : % d" % (key, value))


# Driver function
if __name__ == "__main__":
	my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
	CountFrequency(my_list)

#80
def CountFrequency(my_list):

	# Creating an empty dictionary
	count = {}
	for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
		count[i] = count.get(i, 0) + 1
	return count


# Driver function
if __name__ == "__main__":
	my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
	print(CountFrequency(my_list))

#81
import operator

def CountFrequency(my_list):

	# Creating an empty dictionary
	freq = {}
	for items in my_list:
		freq[items] = operator.countOf(my_list, items)

	for key, value in freq.items():
		print("% d : % d" % (key, value))

# Driver function
if __name__ == "__main__":
	my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
	CountFrequency(my_list)

#82
# Python code to convert into dictionary


def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
		("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))

#83
# Python code to convert into dictionary
list_1 = [("Nakul", 93), ("Shivansh", 45), ("Samved", 65),
		("Yash", 88), ("Vidit", 70), ("Pradeep", 52)]
dict_1 = dict()

for student, score in list_1:
	dict_1.setdefault(student, []).append(score)
print(dict_1)

#84
# Python code to convert into dictionary
def Convert(tup, di):
	di = dict(tup)
	return di
	
# Driver Code 
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
	("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

#85
# Python code to convert into dictionary

print(dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]))

#86
from itertools import groupby


def convert_to_dict(tuple_list):
	# Group the tuples by their first element (the key)
	groups = groupby(tuple_list, key=lambda x: x[0])

	# Create an empty dictionary
	dictionary = {}

	# Iterate over the groups
	for key, group in groups:
		# Extract the second element of each tuple in the group and add it to the dictionary as the value for the key
		dictionary[key] = [tuple[1] for tuple in group]

	return dictionary


# Test the function
tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
			("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(convert_to_dict(tuple_list)) # {'akash':

#87
def convert_to_dict(tuple_list):
	# Create an empty dictionary
	dictionary = {}

	# Iterate over each tuple in the list
	for tuple in tuple_list:
		# Check if the key is already in the dictionary
		if tuple[0] in dictionary:
			# If the key is already in the dictionary, append the value to the existing list
			dictionary[tuple[0]].append(tuple[1])
		else:
			# If the key is not in the dictionary, add it and set the value as a new list
			dictionary[tuple[0]] = [tuple[1]]

	# Return the completed dictionary
	return dictionary


# Test the function
tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
			("suraj", 20), ("akhil", 25), ("ashish", 30)]
# {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
print(convert_to_dict(tuple_list))

#88
def convert_to_dict(tuple_list):
	# Create a dictionary using the dict() constructor and a list comprehension
	dictionary = dict((key, value) for key, value in tuple_list)

	# Return the completed dictionary
	return dictionary


tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
			("suraj", 20), ("akhil", 25), ("ashish", 30)]
# {'akash': 10, 'gaurav': 12, 'anand': 14, 'suraj': 20, 'akhil': 25, 'ashish': 30}
print(convert_to_dict(tuple_list))

#89
# Python code to find if we can make first string
# from second by deleting some characters from
# second and rearranging remaining characters.
from collections import Counter

def makeString(str1,str2):

	# convert both strings into dictionaries
	# output will be like str1="aabbcc",
	# dict1={'a':2,'b':2,'c':2}
	# str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}
	dict1 = Counter(str1)
	dict2 = Counter(str2)

	# take intersection of two dictionaries
	# output will be result = {'a':1,'b':2,'c':2}
	result = dict1 & dict2

	# compare resultant dictionary with first
	# dictionary comparison first compares keys
	# and then compares their corresponding values
	return result == dict1

# Driver program
if __name__ == "__main__":
	str1 = 'ABHISHEKsinGH'
	str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
	if (makeString(str1,str2)==True):
		print("Possible")
	else:
		print("Not Possible")

#90
# Function to Check if frequency of all characters 
# can become same by one removal 
from collections import Counter 

def allSame(input): 
	
	# calculate frequency of each character 
	# and convert string into dictionary 
	dict=Counter(input) 

	# now get list of all values and push it 
	# in set 
	same = list(set(dict.values())) 

	if len(same)>2: 
		print('No') 
	elif len (same)==2 and same[1]-same[0]>1: 
		print('No') 
	else: 
		print('Yes') 

	
	# now check if frequency of all characters 
	# can become same 
	
# Driver program 
if __name__ == "__main__": 
	input = 'xxxyyzzt'
	allSame(input) 

#91
