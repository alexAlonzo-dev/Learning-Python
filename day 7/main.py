import random

lives = 6

word_list = ["ale", "ud6"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for n in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE")

    if "_" not in display:
        game_over = True
    else: 
        game_over = False
