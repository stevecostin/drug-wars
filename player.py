from narcotic import Narcotic

class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.drugs = set()

    def __str__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def add_narcotic(self, narcotic: Narcotic) -> None:
        pass

    def remove_narcotic(self) -> None:
        pass

    def get_narcotic(self, index: int) -> Narcotic:
        pass

    def get_narcotics(self) -> Narcotic:
        pass