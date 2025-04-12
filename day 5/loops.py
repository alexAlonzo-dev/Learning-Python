fruits = ["Watermelon", "Banana", "Strawberry", "Kiwi"]

cont = 1
for fruit in fruits:
    print(f"{cont} {fruit}")
    cont+=1

numbers = [1,2,3,4,5,6,7,8,9,10,420,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10]
plus = 0
min = 0
for n in numbers:
    plus+=n
    if n > min:
        min = n
print(f"Max: {min} \nSize: {len(numbers)} \nSum of values: {sum(numbers)} \nMy Impl: {plus} \nMax using function: {max(numbers)}")

#Loop For using range() function
for n in range(1,11):
    print(f"{n*5}")


#Gaus
gaus = 0
for n in range(1, 101):
    gaus+=n

print(f"Gaus: {gaus}")