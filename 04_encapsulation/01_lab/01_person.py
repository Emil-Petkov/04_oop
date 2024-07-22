class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


person = Person('Emil', 1)
print(person.get_name())
print(person.get_age())

print(person._Person__name)
print(person._Person__age)
