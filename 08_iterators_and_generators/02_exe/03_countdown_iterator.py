class countdown_iterator:
    def __init__(self, number):
        self.number = number + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        self.number -= 1

        return self.number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
