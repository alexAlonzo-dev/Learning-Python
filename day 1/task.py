#this is a comment (it will not be print)
print("Hello Everyone")
print("Printing some: \nLong text? \nNot")
print("Hey" + " You!")

#let's see
print("Hello " +input("Input your name: ") + "!\n")

#function len
name = input("\nInput your name: ")
print("Name: "+name +"\nLength: "+str(len(name)) )

#shortest way
print(len(input("\nEnter name: ")))

#challenge
name = input("\nEnter a name: ")
length = len(name)
print(name)
print(length)


#challenge
print("\nGetting the  name of your band")
nm = input("Input your city name: ")
fv_animal = input("Input name of your favorite pet: ")
print("Your name´s band is: " +nm +" "+fv_animal)