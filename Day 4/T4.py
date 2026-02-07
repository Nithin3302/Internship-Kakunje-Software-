# Task 1
# A = [
#     [2, 4, 6],
#     [8, 0, 1],
#     [3, 5, 7]
# ]

# A.append([10, 11, 12])
# print("After appending row:", A)

# col = [13, 14, 15, 16]
# for i in range(len(A)):
#     A[i].append(col[i])
# print(A)

# A.insert(1, [16, 17, 18, 20])
# print(A)

# col2 = [19, 20, 21, 22, 23]
# for i in range(len(A)):
#     A[i].insert(2, col2[i])
# print(A)

# Task 2
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# print(m[1])
# print([row[2] for row in m])
# print(m[2], m[3])
# print([row[:2] for row in m])
# print(m[2][1:], m[3][1:])
# print([m[1][0], m[1][3]], [m[3][0], m[3][3]])
# print([m[i][i] for i in range(len(m))])
# print([m[i][3-i] for i in range(len(m))])

# Task 3
# A = [
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ]

# col1 = [0, 0, 0]
# for i in range(len(A)):
#     A[i].append(col1[i])
# print(A)

# col2 = [5, 5, 5]
# for i in range(len(A)):
#     A[i].insert(1, col2[i])
# print(A)

# A.append([1, 2, 3, 4, 5])
# print(A)

# A.insert(2, [6, 7, 8, 9, 10])
# print(A)

# col3 = [10, 20, 30, 40, 50]
# for i in range(len(A)):
#     A[i].append(col3[i])
# print(A)

# Task 4
# m = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# print(m[0], m[2], m[4])
# print([row[::2] for row in m])
# print(m[1][:3], m[3][:3])
# print([m[i][i] for i in range(len(m))])
# print([m[i][4-i] for i in range(len(m))])
# print(m[0][::2], m[2][::2], m[4][::2])
# print([m[i][4] for i in range(1, 4)])
# print(m[1][2:4], m[3][2:4])
# print(m[-1])
# print(m[0][1:4:2], m[1][1:4:2], m[2][1:4:2])

# # Task 5
# m = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# # Replace 60 with 6
# m[1][2] = 6
# print(m)

# print(m[0], m[1])
# print(m[1][1:], m[2][1:])
# print([m[i][i] for i in range(len(m))])
# print([m[i][2-i] for i in range(len(m))])
# print([row[1] for row in m])
# print([m[1][0], m[1][2]])
# print([m[0][0], m[2][0]])
# print(m[0][1:], m[2][1:])
# print([m[1][0], m[1][2]], [m[2][0], m[2][2]])

# task6
# A = [
#     [11, 0, 4, 6, 5],
#     [1, 9, 3, 2, 1],
#     [7, 0, 4, 9, 8],
#     [3, 7, 12, 15, 0]
# ]

# print(A[3][2])
# print(A[1][1:4], A[2][1:4])
# print([A[1][1], A[2][1]])
# print(A[1][:3], A[2][:3], A[3][:3])
# print([A[0][0], A[0][2], A[0][4]], [A[3][0], A[3][2], A[3][4]])

# # Add row after the last original row
# A.insert(4, [0, 0, 0, 0, 0])
# print(A)

# print([A[i][i] for i in range(len(A)-1)])
# print([A[i][4] for i in range(len(A)-1)])
# print(A[1], A[2])
# print(A[0][2:4], A[1][2:4], A[2][2:4], A[3][2:4])

# Task 7
B = [
    [9, 8, 7],
    [1, 3, 2],
    [4, 6, 5]
]

print(B[0][1:], B[1][1:])
print(B[2][:2])
print([B[i][i] for i in range(len(B))])
print([B[i][2-i] for i in range(len(B))])

# Add column [1, 1, 1]
for i in range(len(B)):
    B[i].insert(3, 1)
print(B)

print([[B[i][1], B[i][3]] for i in range(len(B))])
print([B[1][0], B[1][3]])

# Add row [0,0,0,0]
B.insert(2, [0, 0, 0, 0])
print(B)

# Add column [10, 10, 10, 10]
for i in range(len(B)):
    B[i].insert(2, 10)
print(B)

print([B[0][1], B[0][3]], [B[3][1], B[3][3]])