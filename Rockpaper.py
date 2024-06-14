import random

opt=("rock","paper","scissor")
player=None
comp=random.choice(opt)
while player not in opt:    
    player=input("Enter a choice (rock,paper,scissors):")

print(f"Player:{player}")
print("Computer:",comp)

if player== comp:
    print("It's a tie!")
elif player=="rock" and comp =="scissor":
    print("You Win!")
elif player=="paper" and comp =="rock":
    print("You Win!")
elif player=="scissor" and comp =="paper":
    print("You Win!")
else:
    print("Computer Win!")


