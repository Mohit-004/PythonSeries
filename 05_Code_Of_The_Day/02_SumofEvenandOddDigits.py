number = int(input('Enter the number : '))

evenSum = 0
oddSu = 0

temp_n = number

while temp_n > 0:
    digit = temp_n % 10

    if digit % 2 == 0 :
        evenSum += digit
    
    else :
        oddSum += digit

    temp_n = temp_n // 10

print(f"Even sum : {evenSum}")
print(f"Odd Sum : {oddSum}")