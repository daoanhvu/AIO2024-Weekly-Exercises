import math
from myutils import is_number

def calc_sig(x):
    return 1.0 / (1.0 + math.exp(-x))

def calc_elu(x, alpha):
    return (alpha * (math.exp(x) - 1.0)) if x <= 0 else x


def calc_activation_func(x, act_name: str):
    if act_name == 'sigmoid':
        return calc_sig(x=x)
    elif act_name == 'relu':
        return 0 if x <= 0 else x
    else:
        alpha = 0.01
        return calc_elu(x = x, alpha=alpha)


def exercise2(x, act_name: str):
    if not is_number(x):
        print("x must be a number.")
        return
    
    lower_af = act_name.lower()
    
    if lower_af != 'sigmoid' and lower_af != 'relu' and lower_af != 'elu':
        print(f'{act_name} is not supported.')
        return
    
    result = calc_activation_func(x=x, act_name=act_name)
        
    print(f'Activation function: {act_name}')
    print(f'{act_name}: f({x}) = {result}')


if __name__ == '__main__':
    exercise2(x=1.2, act_name='sigmoid')
