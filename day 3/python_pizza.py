print("Welcome to Python Pizza Alex's Delivery")
size = input("What size do you prefer? S, M or L: ")
pep = input("Do you want pepperoni on your Pizza? Y or N: ")
ch = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill+= 15

elif size == "M":
    bill+=20

elif size == "L":
    bill+= 25

else:
    print("Type a correct size")

if pep == "Y":
    if size =="S":
        bill += 2
    else:
        bill+= 3

if ch == "Y":
    bill+= 1

print(f"Your final bill is: ${bill}")