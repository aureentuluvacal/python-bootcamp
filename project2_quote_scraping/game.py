import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

def start_game(all_quotes):
  quote = choice(all_quotes)
  remaining_guesses = 4
  guess = ""

  author_response = requests.get(f"{BASE_URL + quote['author_bio_link']}")
  soup = BeautifulSoup(author_response.text, "html.parser")
  author_birth_date = soup.find(class_="author-born-date").get_text()
  author_birth_location = soup.find(class_="author-born-location").get_text()

  print(f"\n{quote['text']}")

  while guess != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"\nWho said this? Guesses left: {remaining_guesses} ")
    remaining_guesses -= 1

    if guess == quote["author"].lower():
      print("\nYou got it right!")
      break
    elif remaining_guesses == 3:
      print(f"\nHere's a hint: The author was born on {author_birth_date} {author_birth_location}")
    elif remaining_guesses == 2:
      print(f"\nHere's a hint: The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
      last_initial = quote["author"].split(" ")[1][0]
      print(f"\nHere's a hint: The author's last name starts with: {last_initial}")
    else:
      print(f"\nSorry you ran out of guesses. The answer was {quote['author']}")

  again = ''

  while again.lower() not in ('y', 'yes', 'n', 'no'):
    play_again = input("\nWould you like to play again (y/n)? ")

    if play_again.lower() in ('yes', 'y'):
      return start_game(all_quotes)
    else:
      print("Ok, goodbye!")
      break

def read_quotes(filename):
  with open(filename) as file:
    csv_reader = DictReader(file)
    return list(csv_reader)

quotes = read_quotes("quotes.csv")
start_game(quotes)
