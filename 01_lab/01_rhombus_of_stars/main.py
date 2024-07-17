from core import print_stars


def main():
    try:
        n = int(input())

        if n <= 0:
            raise ValueError('The number must be positive and greater than zero.')

        print_stars(n)

    except ValueError as e:
        print(f'Invalid input. {e}')


if __name__ == '__main__':
    main()
