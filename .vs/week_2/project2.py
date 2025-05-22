print("Choose an equation to solve:")
print("1. Quadratic Equations (Ax^2 + Bx + C = 0)")
print("2. Cubic Equation (Ax^3 + Bx^2 + Cx + D = 0)")
print("3. Quartic Equation (Ax^4 + Bx^3 + Cx^2 + Dx + E = 0)")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    D = b**2 - 4*a*c
    if D >= 0:
        root1 = (-b + D**0.5) / (2*a)
        root2 = (-b - D**0.5) / (2*a)
        print("Roots:", root1, root2)
    else:
        print("No real roots")

elif choice == "2":
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    print("Solving a cubic equation is complex. Use a calculator or solver tool.")

elif choice == "3":
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))
    print("Solving a quartic equation is complex. Use a calculator or solver tool.")

elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
