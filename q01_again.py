shape = input('Choose "triangle" or "trapezium": ').lower()

if (shape == "triangle") :
    b = int(input("Enter length of the base: "))
    h = int(input("Enter height: "))
    print("Area of the triangle is", b * h / 2)
elif (shape == "trapezium") :
    print("You chose trapezium")
else :
    print("You have chosen poorly.")