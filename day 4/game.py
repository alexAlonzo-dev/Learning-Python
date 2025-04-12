import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

play = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors: "))

pos = [rock, paper, scissors]
pc = random.randint(0,2)

print("Your choose: ")
print(pos[play])

print("\nPC: ")
print(pos[pc])

if (play == 0 and pc == 0) or (play == 1 and pc == 1) or (play == 2 and pc == 2):
    print("NO ONE WIN")
elif (play == 0 and pc == 1) or (play == 1 and pc == 2) or (play == 2 and pc == 0):
    print("YOU LOSE")
elif (play == 0 and pc == 2) or (play == 1 and pc == 0) or (play == 2 and pc == 1):
    print("YOU WIN")
