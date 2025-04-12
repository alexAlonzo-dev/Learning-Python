#Subscripting
print("WERO"[3])

#Integer = Whole number
print(123 + 2)

#Float = Floating point number
print(3.1416)

#Boolean
print(True)
print(False)

#Checking datatype
print(type("Hello"))
print(type(123_456))
print(type(3.1416))
print(type(True))


#Cast
print(int("3") + int("2"))

print("Number of letter in your name: " + str(len(input("Ingresa tu nombre: "))))

#BMI Calculator
heigth = 1.65
weigth = 70
imc = round(weigth / (heigth)**2)
print("IMC = "+str(imc))

#f - Strings
name = "Alex"
fv_number = 10
fv_float_number = 3.1416
score = 420
is_winner = True
print(f"Player : {name} Your numbers are: {fv_number} and {fv_float_number} Your Score: {score} Are you Winner?: {is_winner}")
