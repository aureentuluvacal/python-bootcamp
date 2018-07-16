from card import Card
from random import shuffle

class Deck:

  max_cards = 52

  def __init__(self):
    self.cards = [Card(value, suit) for value in Card.permitted_values for suit in Card.permitted_suits]

  def __repr__(self):
    return f"Deck of {self.count()} cards"

  def count(self):
    return len(self.cards)
  
  def _deal(self, num_to_remove):
    cards_remaining = self.count()
    num_to_remove = min(num_to_remove, cards_remaining)

    if self.count() == 0:
      raise ValueError("All cards have been dealt.")

    dealt = self.cards[-num_to_remove:]
    self.cards = self.cards[:-num_to_remove]
    return dealt

  def shuffle(self):
    if self.count() < Deck.max_cards:
      raise ValueError("Only full decks can be shuffled")
    shuffle(self.cards)
    return self

  def deal_card(self):
    return self._deal(1)[0]

  def deal_hand(self, hand_size):
    return self._deal(hand_size)

d = Deck()
print(d)
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)