# # if it is a tie, repeat the loop
# # if player wins, print "You win!"
# # if computer wins, print "You loose"
# # if player selects an invalid option, print "Invalid option" and repeat the loop

# import random

# pick = ['R', 'P', 'S']
# computer = random.choice(pick)
# player = None

# while player not in pick:
#     player = input("Select option \n").upper()
# # if it is a tie, repeat the loop

# if player == computer:
#     print("Player (" + player + ")" + " : Computer (" + computer + ")")
#     print("That is a tie")
# elif player == 'P':
#     if computer == "S":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You loose")
#     elif computer == "R":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You win!")
# elif player == "R":
#     if computer == "S":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You win!")
#     elif computer == "P":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You loose")
# elif player == "S":
#     if computer == "R":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You loose")
#     elif computer == "P":
#         print("Player (" + player + ")" + " : Computer (" + computer + ")")
#         print("You win!")
    
# if player == 'R' and computer == 'P':
#     print("Player (" + player + ")" + " : Computer (" + computer + ")")
#     print("You win!")
    


import random

pick = ['R', 'P', 'S']
play = True
player_counter = 0
computer_counter = 0

while play == False:
    player = input("Enter your move \n").lower()
    computer = random.choice(pick)
    if player == 'P' and computer == 'R' or  player == 'S' and computer == 'P' or player == 'R' and computer == 'S': 
        print("You win")
        player_counter =+ 1
        play = True

    elif player == 'R'  and computer == 'P' or player == 'P' and computer == 'S' or player == 'S' and computer == 'R':
        print("You loose")
        computer_counter =+ 1
        play = True
    else:
        print("It is a tie")