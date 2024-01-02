#1

list = [10, 25 , 30 , 7, 77]
list.sort()
print("Now it is sorted:", list)

#2

list = [10, 25 , 30 , 7, 77]
list.sort(reverse=True)
print(list)

#3
words = ["apple", "mango" , "banana" , "orange" , "grape"]
words.sort(key=len)
print("Sorted by Length:", words)

#4
words = ["apple", "mango", "banana", "orange", "grape"]
words.sort(key=len, reverse=True)
print("Sorted by Length (in reverse):", words)

#5

people = [("vaibhav", 25), ("sriansh", 30), ("aakansha", 22), ("priyanka", 28)]
people.sort(key=lambda x: x[1])
print("Sorted by Age:", people)

#6

people = [("vaibhav", 25), ("sriansh", 30), ("aakansha", 22), ("priyanka", 28)]
people.sort(key=lambda x: x[1], reverse=True)
print("Sorted by Age:", people)


