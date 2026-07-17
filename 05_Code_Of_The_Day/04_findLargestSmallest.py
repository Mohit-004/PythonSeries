# 🐍 Daily Python Practice — Day 4

# Level: Beginner → Beginner+
# Concept: Loops, Number Manipulation, Digit Counting, Conditional Logic

# Problem: Find the Largest and Smallest Digit

# Write a Python program that takes a positive integer n and finds:

# The largest digit present in the number.
# The smallest digit present in the number.
# The difference between the largest and smallest digit.

# Process the number digit by digit.

# Input

# A single positive integer n.

# Output

# Print the largest digit, smallest digit, and their difference in the following format:

# Largest Digit: <largest>
# Smallest Digit: <smallest>
# Difference: <difference>
# Constraints

# 1 ≤ n ≤ 10¹⁸

# Example 1

# Input:

# 58321

# Output:

# Largest Digit: 8
# Smallest Digit: 1
# Difference: 7

# Explanation:

# The digits are 5, 8, 3, 2, 1.

# Largest digit = 8
# Smallest digit = 1
# Difference = 8 - 1 = 7
# Example 2

# Input:

# 90456

# Output:

# Largest Digit: 9
# Smallest Digit: 0
# Difference: 9

# Explanation:

# The digits are 9, 0, 4, 5, 6.

# Largest digit = 9
# Smallest digit = 0
# Difference = 9 - 0 = 9
# Challenge Rules
# Do not convert the number into a string.
# Do not use max().
# Do not use min().
# Use a loop and digit extraction logic.
# Progress

# Day 1: Conditions and arithmetic ✅
# Day 2: Digit extraction and even/odd logic ✅
# Day 3: Number reversal and palindrome logic
# Day 4: Tracking minimum and maximum values during iteration

# Focus especially on how you initialize the largest and smallest digit variables.

number = int(input("Enter the Number: "))

smallest = 9
largest = 0
temp_num = number

while temp_num > 0 :
    digit = temp_num % 10

    if digit < smallest :
        smallest = digit

    if digit > largest :
        largest = digit

    temp_num = temp_num // 10

print(f"Largest Value: {largest}")
print(f"Smallest Value: {smallest}")
print(f"Difference {largest - smallest}")
