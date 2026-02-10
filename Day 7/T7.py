# # 1. Smallest of two
# n1, n2 = 20, 34
# print("num1 is smaller" if n1 < n2 else "num2 is smaller")

# # 2. Voting
# age = 18
# if age >= 18:
#     print("Eligible to vote")

# # 3. Even/Odd
# num = 8
# print("Even" if num % 2 == 0 else "Odd")

# # 4. Grading
# marks_list = [91, 62, 43]
# for m in marks_list:
#     if m >= 90: print("Grade A")
#     elif m >= 75: print("Grade B")
#     else: print("Fail")

# 1-10
for i in range(1, 11):
    print(i)

# Evens 1-50
for i in range(2, 51, 2):
    print(i)

# Table of 5
for i in range(1, 11):
    print(5 * i)

# Vowel Counter
word = "internship"
count = sum(1 for char in word if char in "aeiouAEIOU")
print(count)

# Sum/Count of Digits
n = int(input("Enter a number: "))
s, c = 0, 0
while n > 0:
    s += n % 10
    c += 1
    n //= 10
print(f"Sum: {s}, Count: {c}")