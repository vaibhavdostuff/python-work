#1
rows = 8
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
        
    print('')

#2
rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

#3
rows = 7
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#4
rows = 7
num = rows
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
    print("\r")

#5
rows = 7
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#6
rows = 7
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

#7
rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\r")

#8
rows = 7
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#9
rows = 4
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')

#10
start = 1
stop = 2
current_num = stop
for row in range(1, 5):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop

