import random


def init():
    move = ['P', 'R', 'S']
    play = False
    
    while play == False:
        player = input("Enter your move: \n").upper()
        computer = random.choice(move)

        if player == 'P' and computer == 'R' or  player == 'S' and computer == 'P' or player == 'R' and computer == 'S': 
            play = True
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You win!")
    
        elif player == 'R'  and computer == 'P' or player == 'P' and computer == 'S' or player == 'S' and computer == 'R':
            play = True
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You loose")

        elif player == computer:
            # play = False
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("That is a tie")

        else:
            print("You have selected an invalid option")
            # play =  False


init()