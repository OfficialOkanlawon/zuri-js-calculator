import random

choices = ['P', 'R', 'S']

computer = random.choice(choices)

player = True

while player == True:
    player = input("Select option \n").upper()
    
    if player == 'P':
        if computer == "S":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You loose")
        elif computer == "R":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You win!")
    elif player == "R":
        if computer == "S":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You win!")
        elif computer == "P":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You loose")
    elif player == "S":
        if computer == "R":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You loose")
        elif computer == "P":
            print("Player (" + player + ")" + " : Computer (" + computer + ")")
            print("You win!")
    else player == computer:
        print("Player (" + player + ")" + " : Computer (" + computer + ")")
        print("That is a tie")
        player = True
# else:
#     print("That not a valid play.")
