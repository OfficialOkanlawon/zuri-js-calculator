import random

pick = ['R', 'P', 'S']
computer = random.choice(pick)
player = input("Enter your choice: ")
if player == computer:
    print("Tie")
elif player == 'R' and computer == 'P':
    print("Computer wins")
elif player == 'R' and computer == 'S':
    print("Player wins")
elif player == 'P' and computer == 'R':
    print("Player wins")
elif player == 'P' and computer == 'S':
    print("Computer wins")
elif player == 'S' and computer == 'R':
    print("Computer wins")
elif player == 'S' and computer == 'P':
    print("Player wins")
else:
    print("Invalid input")
