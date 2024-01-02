#list = [10, 25 , 30 , 7, 77]
#list.sort()
#print("Now it is sorted:", list)

#list = [10, 25 , 30 , 7, 77]
#list.sort(reverse=True)
#print(list)

#words = ["apple", "mango" , "banana" , "orange" , "grape"]
#words.sort(key=len)
#print("Sorted by Length:", words)

#words = ["apple", "mango", "banana", "orange", "grape"]
#words.sort(key=len, reverse=True)
#print("Sorted by Length (in reverse):", words)


people = [("vaibhav", 25), ("sriansh", 30), ("aakansha", 22), ("priyanka", 28)]
people.sort(key=lambda x: x[1])
print("Sorted by Age:", people)


