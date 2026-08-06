print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_multiplier = 1 + tip / 100
pay = (bill / people) * tip_multiplier
print(f"Each person should pay: ${pay:.2f}")