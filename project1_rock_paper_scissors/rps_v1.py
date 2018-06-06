print("...rock...")
print("...paper...")
print("...scissors...")

player1_choice = input("Player 1: ")
print("*****NO CHEATING*****\n\n" * 20)
player2_choice = input("Player 2: ")

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