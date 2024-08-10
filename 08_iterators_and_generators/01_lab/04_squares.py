def squares(number):
    for num in range(1, number + 1):
        yield num * num

    # value = 1
    #
    # while value <= number:
    #     yield value * value
    #
    #     value += 1


print(*squares(5))
print(list(squares(5)))
