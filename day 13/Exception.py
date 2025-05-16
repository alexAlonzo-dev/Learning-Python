try:
    age = int(input("How old are you?: "))

except ValueError:
    print("Enter a Integer number")
    age = int(input("How old are you?: "))

if age >= 25:
    print("You're Older Man")