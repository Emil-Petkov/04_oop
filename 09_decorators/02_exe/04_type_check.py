def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for a in args:
                if not isinstance(a, expected_type):
                    return f'Bad Type'

                return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
