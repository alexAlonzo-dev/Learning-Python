import random

attempts = 0
random_number = random.randint(1, 100)

def game():
    dificulty = input("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':""").lower()

    print(random_number)

    global attempts

    if dificulty == "easy":
        print("You have 10 attempts remaining to guess the number.")
        attempts = 10
    elif dificulty == "hard":
        print("You have 5 attempts remaining to guess the number.")
        attempts = 5

    

    while attempts != 0:
        user_guess = int(input("Make a Guess: "))
        if user_guess == random_number:
            print(f"You guess the number, it was {random_number} you need only {attempts} attempts")
        elif user_guess > random_number:
            print("Too High")
            attempts -= 1
        else:
            print("Too Low")
            attempts -= 1



game()
