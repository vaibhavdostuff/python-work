#1
x = "Hello World"
x = 50
x = 60.5
x = 3j
x = ["vaibhav", "is", "here"] 
x = ("vaibhav", "is", "here") 
x = range(10)  
x = {"name": "vaibhav", "age": 2} 
x = {"vaibhav", "is", "here"} 
x = frozenset({"vaibhav", "is", "here"}) 
x = True
x = b"vaibhav"
x = bytearray(4) 
x = memoryview(bytes(6)) 
x = None

#2
a = 5
print("Type of a: ", type(a)) 

b = 5.0
print("\nType of b: ", type(b)) 

c = 2 + 4j
print("\nType of c: ", type(c)) 


#3
String1 = 'vaibhav is here'
print(String1) 
String1 = "myself vaibhav"
print(String1) 
print(type(String1)) 
String1 = '''myself vaibhav and I am here'''
print(String1) 
print(type(String1)) 

String1 = '''vaibhav 
is 
here'''
print("\nCreating a multiline String: ") 
print(String1) 

#4
String1 = "vaibhav is here"
print(String1)
print(String1[0])
print(String1[-1]) 

#5
List = [] 
print("Initial blank List: ") 
print(List) 
List = ['vaibhav is here'] 
print(List) 
List = ["vaibhav", "is", "here"]
print(List[0]) 
print(List[2]) 
List = [['vaibhav', 'is'], ['here']]
print(List) 

#6
List = ["vaibhav", "is", "here"] 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 
print("Accessing element using negative indexing") 
print(List[-1]) 
print(List[-3]) 