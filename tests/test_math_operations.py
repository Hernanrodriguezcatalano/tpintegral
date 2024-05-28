import unittest
from Utils.math_operations import mcd, mcm

class TestMathOperations(unittest.TestCase):
    def test_mcd(self):
        self.assertEqual(mcd(54, 24), 6)
        self.assertEqual(mcd(48, 18), 6)
        self.assertEqual(mcd(101, 103), 1)

    def test_mcm(self):
        self.assertEqual(mcm(54, 24), 216)
        self.assertEqual(mcm(48, 18), 144)
        self.assertEqual(mcm(101, 103), 10403)

if __name__ == "__main__":
    unittest.main()
