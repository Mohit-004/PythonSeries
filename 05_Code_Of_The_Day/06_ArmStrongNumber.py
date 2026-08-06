# Problem: Armstrong Number Checker

# An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits.

# For example:

# 153 = 1³ + 5³ + 3³ = 153
# 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474

# Write a Python program to determine whether a given positive integer is an Armstrong number.

# Input

# A single positive integer n.

# Output

# Print:

# Armstrong Number

# if the number is an Armstrong number; otherwise print:

# Not an Armstrong Number
# Constraints
# 1 ≤ n ≤ 10⁹
# Example 1

# Input

# 153

# Output

# Armstrong Number

# Explanation

# Number of digits = 3
# 1
# 3
# +5
# 3
# +3
# 3
# =1+125+27=153

# Since the sum equals the original number, it is an Armstrong number.

# Example 2

# Input

# 123

# Output

# Not an Armstrong Number

# Explanation

# Number of digits = 3
# 1
# 3
# +2
# 3
# +3
# 3
# =1+8+27=36

# Since 36 ≠ 123, it is not an Armstrong number.

# Challenge Rules
# Do not convert the number into a string.
# First determine the number of digits using arithmetic operations.
# Then compute the sum of each digit raised to the calculated power.
# Use only loops and arithmetic operators (%, //, **).
# Concepts You'll Practice
# Extracting digits using % 10
# Removing digits using // 10
# Counting the number of digits
# Using exponentiation (**)
# Working with multiple loops
# Comparing computed and original values

number = int(input("Enter the number: "))
temp_number = number
power = 0
res = 0

if number == 0:
    power = 1
else :
    while temp_number > 0:
        power += 1
        temp_number //= 10

temp_number = number
res = 0


while temp_number > 0:
    digit = temp_number % 10
    res = res + digit ** power
    temp_number //= 10

if res == number :
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")