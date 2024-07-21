from typing import List


class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return True if not self.data else False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


s = Stack()
print(s)
print(s.is_empty())
s.push('7')
print(s.top())
s.push('17')
print(s)
print(s.top())
print(s.pop())
s.push('77')
print(s)
s.push('777')
print(s.is_empty())
print(s)
print(s.top())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
print(s)
