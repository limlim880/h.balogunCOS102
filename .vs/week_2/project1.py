# Input names and ages
name1 = input("Enter first name: ")
age1 = input(f"Enter {name1}'s age: ")

name2 = input("Enter second name: ")
age2 = input(f"Enter {name2}'s age: ")

# Swap the ages
temp = age1
age1 = age2
age2 = temp

# Display the swapped results
print("\nAfter swapping:")
print(f"{name1} is now {age1} years old.")
print(f"{name2} is now {age2} years old.")
