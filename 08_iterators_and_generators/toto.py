import random


def random_generator():
    random_numbers = set()

    while len(random_numbers) < 6:
        number = random.randint(1, 49)
        if number not in random_numbers:
            random_numbers.add(number)

            yield number


print(', '.join([str(n) for n in random_generator()]))
