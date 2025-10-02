from drug import Drug

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

    def add_drug(self, drug: Drug) -> None:
        pass

    def remove_drug(self) -> None:
        pass

    def get_drug(self, index: int) -> Drug:
        pass

    def get_drugs(self) -> Drug:
        pass