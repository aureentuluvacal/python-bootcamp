import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1_choice = input("Player 1: ").lower()
player2_choice = random.choice(["rock","paper","scissors"])

print(f"Player 2: {player2_choice}")

if player1_choice == player2_choice:
  print("Draw!")
elif player1_choice == "paper":
  if player2_choice == "scissors":
    print("Player 2 wins!")
  else: 
    print("Player 1 wins!")
elif player1_choice == "rock":
  if player2_choice == "paper":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
elif player1_choice == "scissors":
  if player2_choice == "rock":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
else:
  print("Something went wrong.")