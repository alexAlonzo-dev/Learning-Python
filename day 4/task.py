import random

print(random.randint(1,10))

print(f"Random: {random.random()} Random * 10: {random.random()*10} Floating random: {random.uniform(1,10)}")

tails_or_heads = random.randint(1,2)
if tails_or_heads == 1:
    print("Tails")
else:
    print("Heads")

    