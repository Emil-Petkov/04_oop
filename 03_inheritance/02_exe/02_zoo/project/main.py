from project.lizard import Lizard
from project.mammal import Mammal
from project.snake import Snake

mammal = Mammal('Stella')
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard('John')
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
snake = Snake('Mr. Python')
print(snake.__class__.__bases__[0].__name__)
print(snake.name)
