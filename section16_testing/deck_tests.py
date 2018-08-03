import unittest
from deck import Deck

class DeckTests(unittest.TestCase):
  def setUp(self):
    self.deck = Deck()

  def test_init(self):
    """decks should have a cards list attribute with length 52"""
    self.assertTrue(isinstance(self.deck.cards, list))
    self.assertEqual(len(self.deck.cards), 52)

  def test_repr(self):
    """decks should be represented as 'Deck of COUNT cards'"""
    self.assertEqual(repr(self.deck), "Deck of 52 cards")

  def test_count(self):
    """count should return the number of cards in the deck"""
    self.assertEqual(self.deck.count(), 52)
    self.deck.cards.pop()
    self.assertEqual(self.deck.count(), 51)

  def test_deal_sufficient_cards(self):
    """_deal should deal the number of cards specified if there are enough cards in the deck"""
    cards = self.deck._deal(10)
    self.assertEqual(len(cards), 10)
    self.assertEqual(self.deck.count(), 42)

  def test_deal_insufficient_cards(self):
    """_deal should deal the number of cards left in the deck if there's not enough cards in the deck"""
    cards = self.deck._deal(100)
    self.assertEqual(len(cards), 52)
    self.assertEqual(self.deck.count(), 0)

  def test_deal_no_cards(self):
    """_deal should throw a ValueError if the deck is empty"""
    self.deck._deal(self.deck.count())
    with self.assertRaises(ValueError):
      self.deck._deal(1)

  def test_deal_card(self):
    """deal_cards should deal a single card"""
    card = self.deck.cards[-1]
    dealt_card = self.deck.deal_card()
    self.assertEqual(card, dealt_card)
    self.assertEqual(self.deck.count(), 51)

  def test_deal_hand(self):
    """deal_hand shoudl deal the number of cards passed in"""
    cards = self.deck.deal_hand(20)
    self.assertEqual(len(cards), 20)
    self.assertEqual(self.deck.count(), 32)

  def test_shuffle_full_deck(self):
    """shuffle should shuffle the deck if the deck is full"""
    cards = self.deck.cards[:]
    self.deck.shuffle()
    self.assertNotEqual(cards, self.deck.cards)
    self.assertEqual(self.deck.count(), 52)

  def test_shuffle_not_full_deck(self):
    """shuffle should not shuffle an incomplete deck"""
    self.deck._deal(1)
    with self.assertRaises(ValueError):
      self.deck.shuffle()

if __name__ == "__main__":
  unittest.main()