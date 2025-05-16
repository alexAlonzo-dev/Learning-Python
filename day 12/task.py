#Local Scope
def drink_beer():
    drinking = False
    print(f"Are you dringking?: {drinking}")

drink_beer()
#This gonna print nothing because is outside function -> print(drinking)

#Global Scope
friends = True
def who_drink():
    drinking = True
    print(f"Are you drinking? {drinking} -> With Friends? {friends}")

who_drink()

#Changing Global Scope
enemies = 2

def increase_enemies():
    #This gonna have error -> enemies += 1

    #To change global variable
    global enemies
    enemies += 1
    print(f"Total enemies: {enemies}")

increase_enemies()

#Global Constants
PI = 3.1416