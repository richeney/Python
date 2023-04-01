print("Enter a for triangle or b for trapezium.")
choice = input("Enter a or b: ")
if (choice == "a") :
    b = float(input("Enter length of the base: "))
    h = float(input("Enter height: "))
    print("Area of the triangle is ", float(0.5 * b * h))
elif (choice == "b") :
    a = float(input("Enter length of the top: "))
    b = float(input("Enter length of the base: "))
    h = float(input("Enter height: "))
    print("Area of the trapezium is ", float(0.5 * (a + b) * h))
else :
  print("You have chosen poorly.")
