def logged(func):
    def wrapper(*args, **kwargs):
        return f'you called {func.__name__}{args}\n' \
               f'it returned {func(*args, **kwargs)}'

    return wrapper


@logged
def sum_numbers(*args):
    return 3 + len(args)


print(sum_numbers(4, 4, 4))
