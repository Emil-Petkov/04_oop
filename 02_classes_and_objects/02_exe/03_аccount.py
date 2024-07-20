






















class Account:
    def __init__(self, _id: int, name: str, balance: float = 0) -> None:
        self._id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def debit(self, amount: float) -> float | str:
        if self.balance < amount:
            return 'Amount exceeded balance'

        self.balance -= amount
        return self.balance

    def info(self) -> str:
        return f'User {self.name} with account {self._id} has {self.balance} balance'


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1501))
print(account.info())
