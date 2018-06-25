import random

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
  print(f"Player Score: {player_wins}    Computer Score: {computer_wins}")
  print("...rock...")
  print("...paper...")
  print("...scissors...")

  player_choice = input("Player 1: ").lower()

  if player_choice == "quit" or player_choice == "q":
    break

  computer_choice = random.choice(["rock","paper","scissors"])

  print(f"Computer: {computer_choice}")

  if player_choice == computer_choice:
    print("Draw!")
  elif player_choice == "paper":
    if computer_choice == "scissors":
      print("Computer wins!")
      computer_wins += 1
    else: 
      print("Player 1 wins!")
      player_wins += 1
  elif player_choice == "rock":
    if computer_choice == "paper":
      print("Computer wins!")
      computer_wins += 1
    else:
      print("Player 1 wins!")
      player_wins += 1
  elif player_choice == "scissors":
    if computer_choice == "rock":
      print("Computer wins!")
      computer_wins += 1
    else:
      print("Player 1 wins!")
      player_wins += 1
  else:
    print("Something went wrong.")

print("\nFinal Score")
print("-----------")
print(f"Player: {player_wins}    Computer: {computer_wins}\n")

if player_wins > computer_wins:
  print("Congrats, you won!")
elif player_wins == computer_wins:
  print("It's a tie!")
else: 
  print("Computer wins!")