import unittest
from exercise2 import calc_sig, calc_elu, calc_activation_func

class TestExercise2(unittest.TestCase):
    def test_calc_sig(self):
        assert round(calc_sig(3), 2) == 0.95
        print(round(calc_sig(2), 2))

    def test_calc_sig(self):
        assert round(calc_sig(3), 2) == 0.95
        print(round(calc_sig(2), 2))

    def test_calc_elu(self):
            assert round(calc_elu(1, 0.01)) == 1
            print(round(calc_elu(-1, 0.01), 2))

    def test_activation_function(self):
        assert calc_activation_func(x = 1, act_name='relu') == 1
        print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))


if __name__=='__main__':
    unittest.main()

