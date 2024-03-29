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
