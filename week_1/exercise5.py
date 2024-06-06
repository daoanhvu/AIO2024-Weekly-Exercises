import math
import random


def md_nre_single_sample(y, y_hat, n, p):
    exp_level = 1.0 / n
    tmp = math.pow(y, exp_level) - math.pow(y_hat, exp_level)
    return math.pow(tmp, p)


if __name__ == '__main__':
    n = 3
    p = 4
    for i in range(5):
        y = (random.randint(0, 10) + 0.5) / 10.0
        y_hat = (random.randint(0, 10) + 0.5) / 10.0
        loss = md_nre_single_sample(y=y, y_hat=y_hat, n=n, p=p)
        print(f'y = {y}, y_hat = {y_hat}, loss = {loss}')
