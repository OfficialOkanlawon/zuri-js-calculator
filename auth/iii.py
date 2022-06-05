import random

pick = ['R', 'P', 'S']
play = False
computer = random.choice(pick)
player_counter = 0
computer_counter = 0

while play == False:
    player = input("Enter your move \n").lower()
    
    if player == 'P' and computer == 'R' or  player == 'S' and computer == 'P' or player == 'R' and computer == 'S': 
        play = True
        print("You win")
        player_counter =+ 1

    elif player == 'R'  and computer == 'P' or player == 'P' and computer == 'S' or player == 'S' and computer == 'R':
        play = True
        print("You loose")
        computer_counter =+ 1
else:
    print("It is a tie")