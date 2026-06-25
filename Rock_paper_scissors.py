import random
choices=['stone','paper','scissors']
user=input("Enter a stone, paper or scissors:").lower()
computer=random.choice(choices)
if computer==user:

