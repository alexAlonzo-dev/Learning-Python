print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
n_people = int(input("How many people to split the bill? "))

tip_amount = (tip / 100) * bill

out = (bill + tip_amount) / n_people

print(f"Each person must pay: ${round(out, 2)}")
