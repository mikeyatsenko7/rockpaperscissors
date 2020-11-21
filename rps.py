import random

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

our_choice = input("pick a choice\n")

print("computer choice: ", computer_choice)
print("player choice: ", our_choice)

if our_choice == computer_choice:
print("tie")
elif computer_choice == "rock" and our_choice == "scissors":
print("computer wins")
elif computer_choice == "paper" and our_choice == "rock":
print("computer wins")
elif computer_choice == "scissors" and our_choice == "paper":
print("computer wins")
elif computer_choice == "scissors" and our_choice == "rock":
print("you win")
elif computer_choice == "paper" and our_choice == "scissors":
print("you win")
elif computer_choice == "rock" and our_choice == "paper":
print("you win")
else:
print("you cheater!!!")
