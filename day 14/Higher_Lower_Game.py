import random

celebrities = {
    "Cristiano Ronaldo": 600,
    "Selena Gomez": 430,
    "Dwayne Johnson": 375,
    "Kylie Jenner": 385,
    "Kim Kardashian": 340,
    "Lionel Messi": 455,
    "Ariana Grande": 375,
    "Beyoncé": 320,
    "Justin Bieber": 290,
    "Taylor Swift": 295
}

score = 0

def get_random_celebrities(celebrities):
    return random.sample(list(celebrities.items()), 2)

def play_game():
    global score
    playing = True

    while playing:
        celeb_a, celeb_b = get_random_celebrities(celebrities)
        print(f"A: {celeb_a[0]}")
        print("VS")
        print(f"B: {celeb_b[0]}")

        guess = input("Who has more followers on Instagram? (A/B): ").strip().upper()

        if guess == 'A' and celeb_a[1] >= celeb_b[1] or guess == 'B' and celeb_b[1] >= celeb_a[1]:
            score += 1
            print(f"¡Correct! Points: {score}")
        else:
            print(f"Incorrect. Points: {score}")
            playing = False
            score = 0

if __name__ == "__main__":
    play_game()
