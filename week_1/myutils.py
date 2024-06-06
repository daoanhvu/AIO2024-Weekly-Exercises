

def is_number(n):
    return True if ( isinstance(n, float) or isinstance(n, int) ) else False


def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    f = 1
    for i in range(1, n + 1):
        f = f * i
    
    return f