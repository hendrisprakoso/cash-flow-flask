from functools import wraps


def check_akses(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        print('in Decorator')

        return f(*args, **kwargs)
    return decorator
    
