




from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return f'Not enough space for worker'

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'

        except IndexError:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        money_to_pay = sum([m.salary for m in self.workers])
        if self.__budget >= money_to_pay:
            self.__budget -= money_to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self) -> str:
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])
        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f'You have {len(self.animals)} animals\n'
        lions_in_zoo = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        amount_of_lions = len(lions_in_zoo)
        result += f'----- {amount_of_lions} Lions:\n'
        for lion in lions_in_zoo:
            result += f'{lion}\n'

        tiger_in_zoo = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        amount_of_tigers = len(tiger_in_zoo)
        result += f'----- {amount_of_tigers} Tigers:\n'
        for tiger in tiger_in_zoo:
            result += f'{tiger}\n'

        cheetahs_in_zoo = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        amount_of_cheetahs = len(cheetahs_in_zoo)
        result += f'----- {amount_of_cheetahs} Cheetahs:\n'
        for cheetah in cheetahs_in_zoo:
            result += f'{cheetah}\n'

        return result.strip()

    def workers_status(self) -> str:
        result = f'You have {len(self.workers)} workers\n'

        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']

        result += f'----- {len(keepers)} Keepers:\n'
        for keeper in keepers:
            result += f'{keeper}\n'

        result += f'----- {len(caretakers)} Caretakers:\n'
        for caretaker in caretakers:
            result += f'{caretaker}\n'

        result += f'----- {len(vets)} Vets:\n'
        for vet in vets:
            result += f'{vet}\n'

        return result.strip()
