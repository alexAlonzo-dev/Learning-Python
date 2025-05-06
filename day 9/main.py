is_there_people = True
bids = {}

print("Welcome to Secret Auction")

while is_there_people:
    name = input("Enter your name: ")
    amount = int(input("Enter your amount to auction: "))

    bids[name] = amount

    print("\n" * 100)  

    is_any = input("Is there anyone else who wants to play? (Type 'yes' or 'no'): ").lower()
    if is_any == "no":
        is_there_people = False

highest_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"Congrats {winner}, you win with a bid of: ${highest_bid}")
print("All bids:", bids)
