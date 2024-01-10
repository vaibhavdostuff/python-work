#1
print("first string program python") 

#2 
String1 = '2 string program python'
print(String1) 

String1 = "vaibhav here"
print("\nfirst string program python") 
print(String1) 

String1 = '''vaibhav here'''
print("\nfirst string program python") 
print(String1) 

String1 = '''vaibhav
is
here'''
print("\nfirst string program python") 
print(String1) 

#3
String1 = "vaibhav is here"
print("starting String: ") 
print(String1) 

print("\nFirst character of String is: ") 
print(String1[0]) 

print("\nLast character of String is: ") 
print(String1[-1]) 

#4 
String1 = "vaibhav is here"
print(String1) 

print(String1[1:10]) 

print(String1[1:-2]) 

#5
String1= "vaibhav is here"
print(String1[::-1])

#6
String1= "vaibhav is here"

String1= "1".join(reversed(String1)) 
  
print(String1)

#7
String1 = "Hello,vaibhav is here"
print(String1) 

#1 
list1 = list(String1) 
list1[2] = '1'
String2 = ''.join(list1)
print(String2) 

#2 
String3 = String1[0:2] + '2' + String1[3:] 
print(String3) 

    
#8
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

#1 
list1 = list(String1) 
list1[2] = '1'
String2 = ''.join(list1) 
print(String2) 

#2 
String3 = String1[0:10] + '1' + String1[7:] 
print(String3)

#9
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 


String1 = "working on programm"
print("\nUpdated String: ") 
print(String1) 

#10
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

print("Deleting character at 2nd Index: ") 
#del String1[2] 
print(String1)

#11
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 

String2 = String1[0:10] + String1[7:] 
print("\nDeleting character at 2nd Index: ") 
print(String2) 

#12
String1 = "Hello,vaibhav is here"
print("Initial String: ") 
print(String1) 


del String1 
print("\nDeleting entire String: ") 
#print(String1) 

#13
String1 = '''Hello,vaibhav is here'''
print(String1) 


String1 = 'Hello,vaibhav is here'
print(String1) 


String1 = "Hello,vaibhav is here"
print(String1) 

String1 = "C:\\Python\\string\\"
print(String1)
  

String1 = "Hi\tstring"
print("\nTab: ") 
print(String1) 
  

String1 = "Python\nstring"
print("\nNew Line: ") 
print(String1) 

#14
# Printing hello in octal 
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1)
