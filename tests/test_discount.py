import unittest

from aims.discount import Discount


class TestDiscount(unittest.TestCase):
    def test_calculate_discount(self):
        result = Discount.calculate_discount(100, 20)
        self.assertEqual(result, 80)

    def test_invalid_discount_percent(self):
        with self.assertRaises(ValueError):
            Discount.calculate_discount(100, 150)


if __name__ == "__main__":
    unittest.main()
    