rows = 8
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
        
    print('')


rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')


rows = 7
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

rows = 7
num = rows
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
    print("\r")

rows = 7
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

rows = 7
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

