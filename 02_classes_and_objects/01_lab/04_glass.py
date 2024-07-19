class Glass:
    capacity = 250  # ml

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml_liquid: int) -> str:
        if self.content + ml_liquid <= Glass.capacity:
            self.content += ml_liquid
            return f'Glass filled with {ml_liquid} ml'

        return f'Cannot add {ml_liquid} ml'

    def empty(self) -> str:
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        result = abs(self.content - Glass.capacity)
        return f'{result} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
