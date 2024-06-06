import unittest
import math
from myutils import factorial, is_number

class TestMyUtils(unittest.TestCase):
    
    def test_factorial(self):
        for i in range(1000):
            self.assertEqual(math.factorial(i), factorial(i))


    def test_is_number(self):
        assert is_number(3) == 1.0
        assert is_number('-2a') == 0.0
        print(is_number(1))
        print(is_number('n'))


if __name__=='__main__':
    unittest.main()
