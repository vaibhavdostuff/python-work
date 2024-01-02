#list = [10, 25 , 30 , 7, 77]
#list.sort()
#print("Now it is sorted:", list)

#list = [10, 25 , 30 , 7, 77]
#list.sort(reverse=True)
#print(list)

#words = ["apple", "mango" , "banana" , "orange" , "grape"]
#words.sort(key=len)
#print("Sorted by Length:", words)

words = ["apple", "mango", "banana", "orange", "grape"]
words.sort(key=len, reverse=True)
print("Sorted by Length (in reverse):", words)
