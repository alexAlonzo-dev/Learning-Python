def greet():
    print("Mexican")
    print("American")
    print("Japanese")

greet()

#Function that allows input
def greet_name(name):
    print(f"Hello {name}")

greet_name("alex")


#Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name} \nHow is the weather in {location}?")

greet_with("alex", "Chilitos")