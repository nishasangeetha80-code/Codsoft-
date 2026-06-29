import random

choices = ["stone", "paper", "scissors"]

user = input("Enter stone, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "stone" and computer == "scissors") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")