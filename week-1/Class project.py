while True:
    print("\nSelect an option:")
    print("1: Simple Interest")
    print("2: Compound Interest")
    print("3: Annuity Plan")
    print("4: Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        P = float(input("enter principal: "))
        R = float(input("Enter rate: "))
        T = float(input("Enter time: "))
        SI = P * (1 + (R / 100) * T)
        print("Result:", SI)

    elif choice == '2':
        P = float(input("Enter principal: "))
        R = float(input("Enter rate: ")) / 100
        n = int(input("Enter number of times compounded: "))
        t = float(input("Enter time: "))
        CI = P * (1 + R / n) ** (n * t)
        print("Result:", CI)

    elif choice == '3':
        PMT = float(input("Enter payment amount: "))
        R = float(input("Enter rate: ")) / 100
        n = int(input("Enter payments per year: "))
        t = float(input("Enter time: "))
        R_n = R / n
        A = PMT * (((1 + R_n) ** (n * t) - 1) / R_n)
        print("Result:", A)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid input. Try again.")

    again = input("Do another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Exiting... ")
        break
