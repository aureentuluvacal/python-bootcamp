import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
  def test_eat_healthy(self):
    """Eat should have a positive message for healthy eating"""
    self.assertEqual(
      eat("broccoli", is_healthy=True),
      "I'm eating broccoli because my body is a temple."
    )

  def test_eat_unhealthy(self):
    """Eat should have a fuck it message for unhealthy eating"""
    self.assertEqual(
      eat("pizza", is_healthy=False),
      "I'm eating pizza because YOLO!"
    )

  def test_short_nap(self):
    """Napping for less than 2 hours should be refreshing."""
    self.assertEqual(
      nap(1),
      "I feel refreshed after my 1 hour nap!"
    )

  def test_long_nap(self):
    """Napping for over two hours is oversleeping."""
    self.assertEqual(
      nap(3),
      "No! I overslept! I didn't mean to nap for 3 hours!"
    )

if __name__ == "__main__":
  unittest.main()