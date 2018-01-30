#Calculates the area of a rectangle
print("This program calculates the area of a rectangle")
while True:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    Area = length * width
    print("The Area of the Rectangle is", Area)
    answer = input("Would you like to calculate the Area of a new rectangle? Y/N")
    if answer == "Y" or answer == "y":
        continue
    else:
        break
