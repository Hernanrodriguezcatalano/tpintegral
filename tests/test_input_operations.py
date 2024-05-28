import unittest
from unittest.mock import patch
from Utils.input_operations import get_int

class TestInputOperations(unittest.TestCase):
    @patch('builtins.input', side_effect=['a', '5'])
    def test_get_int(self, mock_input):
        self.assertEqual(get_int(), 5)

if __name__ == "__main__":
    unittest.main()
