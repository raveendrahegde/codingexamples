from functools import wraps

def dec_4x(func):
    @wraps(func) # To preserve calling function name
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 4
    return wrapper

def multipy_nx(n):
    def dec_nx(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * n
        return wrapper
    return dec_nx

@dec_4x
def add_two(num):
    return num + 2

@multipy_nx(2)
def add_three(num):
    return num + 3

if __name__ == '__main__':
    print(add_two(10))
    print(add_three(10))
    print(add_two.__name__)
    print(add_three.__name__)
