import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_cart_limit(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(title=f"DVD {i + 1}")
            self.assertTrue(cart.add_dvd(dvd))

        dvd_21 = DigitalVideoDisc(title="DVD 21")
        self.assertFalse(cart.add_dvd(dvd_21))


if __name__ == "__main__":
    unittest.main()