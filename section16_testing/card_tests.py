import unittest
from card import Card

class CardTests(unittest.TestCase):
  def setUp(self):
    self.card = Card('A', 'Spades')

  def test_init(self):
    """cards should have a suit and a value"""
    self.assertEqual(self.card.suit, 'Spades')
    self.assertEqual(self.card.value, 'A')

  def test_repr(self):
    """cards should be represented as 'VALUE of TYPE'"""
    self.assertEqual(repr(self.card), 'A of Spades')

if __name__ == "__main__":
  unittest.main()