import random

def who_win(score_player1, score_player2):
    if score_player1 > 21 and score_player2 > 21:
        return "Both lose"
    elif score_player1 > 21:
        return "Computer wins"
    elif score_player2 > 21:
        return "You win"
    elif score_player1 == score_player2:
        return "Tie"
    elif score_player1 > score_player2:
        return "You win"
    else:
        return "Computer wins"

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def display_cards(player_cards, computer_cards):
    print(f"Computer cards: [{computer_cards[0]} and ?]")
    print(f"Your cards: {player_cards}")

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    print(f"Welcome to Blackjack\n")
    
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    
    display_cards(user_cards, computer_cards)


    while input("Do you want an extra card? Type 'y' or 'n': ").lower() == "y":
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        if user_score > 21:
            break
        display_cards(user_cards, computer_cards)
    
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)


    display_cards(user_cards, computer_cards)
    print(f"\nYour final score: {user_score}")
    print(f"Computer's final score: {computer_score}")
    
    result = who_win(computer_score, user_score)
    print(result)

if __name__ == "__main__":
    main()
