class Card:

  permitted_suits = ("Hearts", "Clubs", "Diamonds", "Spades")
  permitted_values = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

  def __init__(self, value, suit):
    if value not in Card.permitted_values:
      raise ValueError(f"Value must be one of {Card.permitted_values}")

    if suit not in Card.permitted_suits:
      raise ValueError(f"Suit must be one of {Card.permitted_suits}")

    self.value = value
    self.suit = suit

  def __repr__(self):
    return f"{self.value} of {self.suit}"

c = Card("A", "Spades")

print(c)