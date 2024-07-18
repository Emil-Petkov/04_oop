class Circle:
    pi = 3.14

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        result = Circle.pi * self.radius ** 2
        return result

    def get_circumference(self) -> float:
        result = 2 * Circle.pi * self.radius
        return result


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
