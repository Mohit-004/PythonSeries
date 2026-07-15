# 🐍 Daily Python Practice — Day 3

# Level: Beginner
# Concept: Loops, Number Manipulation, Digit Logic

# Problem: Reverse a Number and Check Palindrome

# Write a Python program that takes a positive integer n.

# Your program must:

# Reverse the given number.
# Print the reversed number.
# Check whether the original number is a palindrome.

# A number is a palindrome if it remains the same when reversed.

# Input

# A single positive integer n.

# Output

# Print the reversed number.

# Then print:

# Palindrome

# if the number is a palindrome.

# Otherwise, print:

# Not Palindrome
# Constraints

# 1 ≤ n ≤ 10¹⁸

# Example 1

# Input:

# 121

# Output:

# Reversed Number: 121
# Palindrome

# Explanation: The reverse of 121 is 121, so it is a palindrome.

# Example 2

# Input:

# 12340

# Output:

# Reversed Number: 4321
# Not Palindrome

# Explanation: The reverse of 12340 is 4321, which is not equal to the original number.

number = int(input("Enter the number: "))
reverse_number = 0
temp_num = number

while temp_num > 0:
    digit = temp_num % 10
    reverse_number = (reverse_number * 10) + digit

    temp_num = temp_num // 10

print(f"Reversed Number: {reverse_number}")

if number == reverse_number:
    print("Number is Palindrome.")

else :
    print("Number is not plaindrome.")