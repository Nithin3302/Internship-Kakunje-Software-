# def get_product(x, y):
#     return x * y

# print(f"Result: {get_product(5, 3)}")

# def is_even(val):
#     return "Even" if val % 2 == 0 else "Odd"

# print(is_even(7))

# def find_top_value(n1, n2, n3):
#     return max(n1, n2, n3)

# print("Highest number is:", find_top_value(4, 9, 6))

# def compute_factorial(number):
#     total = 1
#     for unit in range(1, number + 1):
#         total *= unit
#     return total

# print(f"Factorial output: {compute_factorial(5)}")

# def total_vowels(phrase):
#     vowel_list = "aeiouAEIOU"
#     return sum(1 for letter in phrase if letter in vowel_list)

# print("Vowel count:", total_vowels("Python"))

# def flip_text(string_data):
#     return string_data[::-1]

# print(flip_text("Hello"))

# def check_prime_status(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(check_prime_status(11))

# def welcome_user(user="Guest"):
#     print(f"Hi there, {user}")

# welcome_user()
# welcome_user("rithesh")

# def show_student_info(name, age):
#     print(f"Student: {name} | Age: {age}")

# show_student_info(age=20, name="Nithin")

# def fib_calc(n):
#     if n <= 1:
#         return n
#     return fib_calc(n-1) + fib_calc(n-2)

# for i in range(7):
#     print(fib_calc(i), end=" ")
# print() 

# power_of_two = lambda n: n**2
# print(f"Square result: {power_of_two(6)}")

try:
    numerator = int(input("Provide a number: "))
    denominator = int(input("Provide a divisor: "))
    print(numerator / denominator)
except ZeroDivisionError:
    print("Error: You can't divide by zero.")

try:
    val = int(input("Input an integer: "))
    print(f"Data received: {val}")
except ValueError:
    print("That was not a valid integer.")

try:
    digit = int(input("Enter a value: "))
    print(f"Squared: {digit**2}")
except:
    print("An unexpected error occurred.")

try:
    entry = int(input("Enter a digit: "))
except ValueError:
    print("Processing failed: Invalid input.")
else:
    print(f"Success! You entered {entry}")

try:
    score = int(input("Enter a number to divide 10 by: "))
    print(10 / score)
except ZeroDivisionError:
    print("Division failed.")
finally:
    print("Cleanup and final steps complete.")

try:
    combine = "Age: " + 25 
except TypeError:
    print("Caught a type mismatch.")

try:
    data = int(input("Enter a number: "))
    print(100 / data)
except (ValueError, ZeroDivisionError) as err:
    print(f"Issue detected: {err}")

user_age = int(input("How old are you? "))
if user_age < 18:
    raise Exception("Access denied: Must be 18+")
else:
    print("Access granted.")