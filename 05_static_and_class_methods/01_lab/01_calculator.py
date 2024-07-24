from functools import reduce


class Calculator:
    @staticmethod
    def add(*numbers) -> int:
        return sum(numbers)

    @staticmethod
    def multiply(*numbers) -> int:
        return reduce(lambda x, y: x * y, numbers)

    @staticmethod
    def divide(*numbers) -> int:
        return reduce(lambda x, y: x / y, numbers)

    @staticmethod
    def subtract(*numbers) -> float:
        return reduce(lambda x, y: x - y, numbers)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
