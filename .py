# print("this is my python programming space")
arr = [1, 2, 3, 4, 5];     
     
print("Elements of given array: ");     
    
for i in range(0, len(arr)):    
    print(arr[i]),
 
print("Array in reverse order: ");    
  
for i in range(len(arr)-1, -1, -1):     
    print(arr[i]),    

    
sum = 0;    
         
for i in range(0, len(arr)):    
   sum = sum + arr[i];    
     
print("Sum of all the elements of an array: " + str(sum));    
