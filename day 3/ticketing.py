heigth = int(input("Write your weigth in cm: "))
bill = 0

if heigth >= 120:
    print("You can ride")
    age = int(input("What is your age: "))

    if age <= 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif 45 <= age <= 55:
        print("Everything gonna be OK")  
    else: 
        print("Adult tickets are $12")
        bill = 12

    wants_photo = input("Do you wanna have a photo take? Type y for Yes and n for No: ")
    if wants_photo == "y":
        bill+=3
    
    print(f"Your final bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride")