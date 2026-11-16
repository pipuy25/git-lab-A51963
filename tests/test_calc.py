import unittest
from app.calc import add, sub, div, sqrt_num

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(5, 0), "Loi: Khong the chia cho 0")

    def test_sqrt(self):
        self.assertEqual(sqrt_num(9), 3.0)
        with self.assertRaises(ValueError):
            sqrt_num(-1)

if __name__ == "__main__":
    unittest.main()
