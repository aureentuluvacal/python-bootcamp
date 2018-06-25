import random

random_number = random.randint(1, 10)

while True:
  guess = input("Pick a number from 1 to 10. ")
  guess = int(guess)

  if guess > random_number:
    print("Too high.")
  elif guess < random_number:
    print("Too low.")
  else:
    print("You guessed it!")
    play_again = input("Would you like to play again? (y/n) ")

    if play_again == "y":
      random_number = random.randint(1, 10)
      guess = None
    else:
      print("Thanks for playing.")
      break