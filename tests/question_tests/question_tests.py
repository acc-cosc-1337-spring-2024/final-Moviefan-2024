import unittest
from question_a import calculate_statistics

class TestCalculateStatistics(unittest.TestCase):
    def test_normal_case(self):
        numbers = [3, 6, 9, 12, 15]
        result = calculate_statistics(numbers)
        self.assertEqual(result, (3, 15, 45, 9))

    def test_invalid_input(self):
        numbers = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            calculate_statistics(numbers)

if __name__ == "__main__":
    unittest.main()
