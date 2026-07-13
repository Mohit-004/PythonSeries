units = int(input("Enter the units consumed: "))

bill = 0

if units <= 100 :
    bill = units * 5

elif units <= 200 :
    bill = 100 * 5 + ((units - 100) * 7)

#elif units > 200 :
 # no need for elif directly use the else because previous condtions are already checked.

else :
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(f"Total Electricity Bill: {bill}.")