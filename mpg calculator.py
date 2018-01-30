#Build a calculator
print("This program calculates miles per gallon")
while True:
    milesDriven = float(input("Enter miles Driven:"))
    gallonsUsed = float(input("Enter Gallons Used: "))
    mpg = milesDriven / gallonsUsed
    print("Miles per gallon = ", mpg)
    answer = input("Would you like to continue mpg Calculator? Yes/No")
    if answer == "Yes" or "yes":
        continue
    else:
        break 

  

