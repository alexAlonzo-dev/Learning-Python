print('''
            _"_ %
           (<  ?
            ` "
           __||___
          |\___//_
        __|\ , /  |/
       /:  /   \  ::
       \| ######o /|
         ######## \)
         ########
          \ :  /
           \: /
            --
            %%%
             %%
              %
             /:
      ''')

print("Welcome to Treasure Island. You have to find the Treasure")
side = input("Wich side do you want to start? Left or Right: ")
if side == "Left" or side == "l":
    decide = input("Do you wanna swim or wait? ")
    if decide == "wait" or decide == "w":
        color = input("Wich door do you choose? Red, Blue or Yellow: ")
        if color == "Yellow" or color == "y":
            print("YOU WIN!")
        elif color == "Red" or color == "r":
            print("Burned by Fire. GAME OVER")
        elif color == "Blue" or color == "b":
            print("Eaten by Beasts. GAME OVER")
        else: 
            print("GAME OVER")
    else:
        print("Attacked by trout. GAME OVER")
else:
    print("Fall into a hole. GAME OVER")
