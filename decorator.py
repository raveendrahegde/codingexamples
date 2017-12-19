def dec_4x(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 4
    return wrapper

@dec_4x
def add_two(num):
    return num + 2

if __name__ == '__main__':
    print(add_two(10))
