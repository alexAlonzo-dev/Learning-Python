def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def multiply(a, b):
    return a * b

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}

def calculator():
    still_playing = True

    while still_playing:
        print("WELCOME TO MY FIRST PYTHON CALCULATOR")
        a = float(input("Type the first number: "))
        op = input("""
    Choose the operation:
    +
    -
    *
    /
    """)
        b = float(input("Type the second number: "))

        if op in operations:
            result = operations[op](a, b)
            print(f"Result: {result}")
        else:
            print("Invalid operation")
            continue

        while True:
            next_step = input("Do you want to continue with the result? (y/n/o to exit): ").lower()
            if next_step == "y":
                op = input("""
    Choose the operation:
    +
    -
    *
    /
    """)
                b = float(input("Type the next number: "))
                if op in operations:
                    result = operations[op](result, b)
                    print(f"Result: {result}")
                else:
                    print("Invalid operation")
            elif next_step == "n":
                break
            elif next_step == "o":
                still_playing = False
                break
            else:
                print("Invalid input. Please enter 'y', 'n', or 'o'.")

calculator()