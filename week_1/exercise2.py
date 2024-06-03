import math
from myutils import is_number

def exercise2(x, activation_function: str):

    if not is_number(x):
        print("x must be a number.")
        return
    
    lower_af = activation_function.lower()
    
    if lower_af != 'sigmoid' and lower_af != 'relu' and lower_af != 'elu':
        print(f'{activation_function} is not supported.')
        return
    
    if lower_af == 'sigmoid':
        result = 1.0 / (1.0 + math.exp(-x))
    elif lower_af == 'relu':
        result = 0 if x <= 0 else x
    elif lower_af == 'elu':
        alpha = 0.01
        result = (alpha * (math.exp(x) - 1.0)) if x <= 0 else x
        
    print(f'Activation function: {activation_function}')
    print(f'{activation_function}: f({x}) = {result}')


if __name__ == '__main__':
    exercise2(x=1.2, activation_function='sigmoid')