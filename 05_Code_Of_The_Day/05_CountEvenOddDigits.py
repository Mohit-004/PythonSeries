# Problem: Count Even and Odd Digits

# Write a Python program that takes a positive integer n and counts:

# The number of even digits.
# The number of odd digits.
# Determine whether the number contains more even digits, more odd digits, or an equal number of both.

# Process the number digit by digit.

# Input

# A single positive integer n.

# Output

# Print the following:

# Even Digits: <count>
# Odd Digits: <count>
# Result: <More Even Digits / More Odd Digits / Equal>
# Constraints
# 1 ≤ n ≤ 10¹⁸
# Example 1

# Input

# 248731

# Output

# Even Digits: 3
# Odd Digits: 3
# Result: Equal

# Explanation

# Even digits: 2, 4, 8
# Odd digits: 7, 3, 1

# Example 2

# Input

# 9024685

# Output

# Even Digits: 5
# Odd Digits: 2
# Result: More Even Digits

# Explanation

# Even digits: 9̶ (odd), 0, 2, 4, 6, 8 → 5 even digits
# Odd digits: 9, 5 → 2 odd digits

# Challenge Rules
# Do not convert the number into a string.
# Do not use lists or arrays.
# Use only arithmetic operations (%, //) and a loop to process each digit.
# What You'll Practice
# Extracting digits using % 10
# Removing digits using // 10
# Counting with variables
# Using if-else statements
# Comparing computed results

number = int(input("Enter the number: "))
evenCount = 0
oddCount = 0
temp_number = number
while temp_number > 0 :
    digit = temp_number % 10

    if digit % 2 == 0 : evenCount = evenCount + 1
    else: oddCount = oddCount + 1

    temp_number //= 10

print(f"Even Digits: {evenCount}")
print(f"Odd Digits: {oddCount}")

if evenCount >  oddCount :
    print(f"Result : More Even Digits")

elif evenCount <  oddCount :
    print(f"Result : More Odd Digits")

else :
    print(f"Result : Equal")
