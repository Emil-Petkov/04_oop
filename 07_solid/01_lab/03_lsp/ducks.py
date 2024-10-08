from abc import abstractmethod, ABC


class QuackMixin:
    @staticmethod
    def quack():
        return 'quack'


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(QuackMixin):
    ...


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


class RealDuck(Duck):
    @staticmethod
    def quack():
        return 'Real duck quacking'

    @staticmethod
    def walk():
        return 'Real duck walking'

    def fly(self):
        return 'Real duck flying'


realD = RealDuck()
rd = RubberDuck()
roboD = RobotDuck()
print(realD.quack())
print(realD.walk())
print(realD.fly())
print(rd.quack())
print(roboD.quack())
print(roboD.quack())
print(roboD.quack())
