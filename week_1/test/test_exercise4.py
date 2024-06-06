import unittest
from exercise4 import approx_sin, approx_cos, approx_cosh, approx_sinh

class TestExercise4(unittest.TestCase):
    def test_approx_cos(self):
        assert round(approx_cos(x=1, n=10), 2) == 0.54
        print(round(approx_cos(x=3.14, n=10), 2))

    def test_approx_sin(self):
        assert round(approx_sin(x=1, n=10), 4) == 0.8415
        print(round(approx_sin(x=3.14, n=10), 4))

    def test_approx_sinh(self):
        assert round(approx_sinh(x=1, n=10), 2) == 1.18
        print(round(approx_sinh(x=3.14, n=10), 2))

    def test_approx_cosh(self):
        assert round(approx_cosh(x=1, n=10), 2) == 1.54
        print(round(approx_cosh(x=3.14, n=10), 2))


if __name__=='__main__':
    unittest.main()