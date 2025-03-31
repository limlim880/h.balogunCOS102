experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))

if experience > 25 and age >= 55:
    atr = 5600000
elif experience > 20 and age >= 45:
    atr = 4480000
elif experience > 10 and age >= 35:
    atr = 1500000
else:
    atr = 550000

print("Annual Tax Revenue (ATR): N" + str(atr))
