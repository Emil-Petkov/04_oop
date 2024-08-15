def even_parameters(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, int) and a % 2 == 0:
                continue

            return f'Please use only even numbers!'

        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
