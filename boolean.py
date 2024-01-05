#1

a = True
type(a)

b = False
type(b)

#2
x = 5
y = 10
print(bool(x==y))

#3
x = None
print(bool(x))

#4
x = ()
print(bool(x))

#5
x = 'VAIBHAV NEGI'
print(bool(x))

#6
x = 0
print(bool(x))
 
y = 1
print(bool(y))
 
z = -10.10
print(bool(z))

#6
x = 1
y = 2
z = 4
 
if x > y or y < z:
    print(True)
else:
    print(False)
 
if x or y or z:
    print("Atleast one number has boolean value as True")


#7

x = 0
y = 2
z = 4
 
if x > y and y<z:
    print(True)
else:
    print(False)
     
if x and y and z:
    print("All the numbers has boolean value as True")
else:
    print("Atleast one number has boolean value as False")


#8
x = 0
 
if not x:
    print("Boolean value of x is False")
