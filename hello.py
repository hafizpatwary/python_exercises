#blackjack
import random

playing = input("Welcome to black Jack, \nPress any key to play or q to quit: ").lower()

while playing != 'q':

    try:
        card1 = int(input("First card: "))
        card2 = int(input("Second card: "))
        
    except ValueError as error:
        print("Enter a number")
        continue
    except NameError as error:
        print("Enter a number")
        continue

    if (card1 or card2) < 0:
        print("Enter number above zero")
        playing #= input("Press any key to keep playing or 'q' to quit: ").lower()
    else:
        if card1 > 21 and card2 > 21:
            print('0')
        elif (card1 > card2) and card1 < 22:
            print(card1)
        elif card2 < 22:
            print(card2)

    playing = input("Press any key to keep playing or 'q' to quit: ").lower()


##    finally:
##        playing = input("Press any key to play again or q to quit: ").lower()
    
