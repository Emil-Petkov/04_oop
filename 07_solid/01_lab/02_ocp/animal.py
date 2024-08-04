from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        ...

    def get_species(self):
        return self.__class__.__name__


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bau-bau'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Mouse()]

animal_sound(animals)
