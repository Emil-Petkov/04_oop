from abc import ABC, abstractmethod


@abstractmethod
class Food(ABC):
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


class Vegetable(Food):
    ...


class Fruit(Food):
    ...


class Meat(Food):
    ...


class Seed(Food):
    ...
