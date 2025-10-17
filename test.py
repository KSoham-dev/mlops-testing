import unittest

class TestModel(unittest.TestCase):
  def test_case1(self):
    self.assertEqual(True, True)

  def test_case2(self):
    self.assertEqual("Soham", "Soham")

  def test_case3(self):
    self.assertEqual("K", "K")
  

if __name__ == "__main__":
  unittest.main()