A = [
    [2, 4, 6],
    [8, 0, 1],
    [3, 5, 7]
]

A.append([10, 11, 12])
print("After appending row:", A)

col = [13, 14, 15, 16]
for i in range(len(A)):
    A[i].append(col[i])
print(A)

A.insert(1, [16, 17, 18, 20])
print(A)

col2 = [19, 20, 21, 22, 23]
for i in range(len(A)):
    A[i].insert(2, col2[i])
print(A)