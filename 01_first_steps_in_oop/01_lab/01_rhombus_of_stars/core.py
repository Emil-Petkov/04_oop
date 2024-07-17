def print_stars(n):
    print_first_part(n)
    print_second_part(n)


def print_row(row, n):
    print(' ' * (n - row), '* ' * row)


def print_first_part(n):
    for row in range(n + 1):
        print_row(row, n)


def print_second_part(n):
    for row in range(n - 1, -1, -1):
        print_row(row, n)

