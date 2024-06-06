import unittest
from exercise3 import calc_ae, calc_se

class TestExercise3(unittest.TestCase):
    def test_calc_ae(self):
        y = 1
        y_hat = 6
        assert calc_ae(y=y, y_hat=y_hat) == 5
        y = 2
        y_hat = 9
        print(calc_ae(y, y_hat))


    def test_calc_se(self):
        y = 4
        y_hat = 2
        assert calc_se(y=y, y_hat=y_hat) == 4
        print(calc_se(2, 1))


if __name__=='__main__':
    unittest.main()