class Weapon:
    def __init__(self, long_name: str, short_name: tuple):
        self.long_name = long_name
        self.short_name = short_name

    def __eq__(self, other) -> bool:
        if isinstance(other, Weapon):
            return self.long_name == other.get_long_name()
        else:
            return NotImplemented

    def get_long_name(self) -> str:
        return self.long_name

    def get_short_name(self) -> tuple:
        return self.short_name


class Knife(Weapon):
    def __init__(self) -> None:
        super().__init__("Knife", ("Dagger",))