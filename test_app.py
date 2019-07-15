import unittest
from afolabi_tope_greater import whichIsGreater
import afolabi_tope_lineOverlap

class GeneralCase(unittest.TestCase):
    def test_greater(self):
        input_values = [3, 2]
        def mock_input():
            return input_values.pop(0)
        whichIsGreater.input = mock_input
        self.assertEqual(whichIsGreater(), "3 is greater than 2")

    def test_overlap(self):
        input_values = ["2, 5", "3, 9"]
        def mock_input():
            return input_values.pop(0)
        afolabi_tope_lineOverlap.input = mock_input
        self.assertEqual(afolabi_tope_lineOverlap.isLineOverLap(), "this two lines overlap")

def main():
    unittest.main()

if __name__ == "__main__":
    main()