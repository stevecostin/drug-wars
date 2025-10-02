# Narcotic should only be inherited from another class
class Narcotic:
    def __init__(self, long_name: str, short_name: tuple, overdose_can_kill_you: bool) -> None:
        self.price = 0
        self.possess_num_of_grams = 0
        self.long_name = long_name
        self.short_name = short_name
        self.overdose_can_kill_you = overdose_can_kill_you

    def __eq__(self, other) -> bool:
        if isinstance(other, Narcotic):
            return self.long_name == other.get_long_name()
        else:
            return NotImplemented

    def get_long_name(self) -> str:
        return self.long_name

    def get_short_name(self) -> tuple:
        return self.short_name

    def set_price_per_gram(self, price: int) -> None:
        self.price = price

    def get_price_per_gram(self) -> int:
        return self.price

    def add_narcotic_to_possession(self, num_of_grams: int) -> None:
        self.possess_num_of_grams += num_of_grams

    def remove_narcotic_from_possession(self, num_of_grams: int) -> None:
        self.possess_num_of_grams -= num_of_grams

    def get_narcotic_possession(self) -> int:
        return self.possess_num_of_grams

    def set_overdose_can_kill_you(self,  overdose_can_kill_you: bool) -> None:
        self.overdose_can_kill_you = overdose_can_kill_you

    def get_overdose_can_kill_you(self) -> bool:
        return self.overdose_can_kill_you


class Weed(Narcotic):
    def __init__(self):
        super().__init__("Marijuana", ("Weed", "Ganja", "Joint", "Spliff"), False)


class Cocaine(Narcotic):
    def __init__(self):
        super().__init__("Cocaine", ("Coke",), True)


class Methamphetamine(Narcotic):
    def __init__(self):
        super().__init__("Methamphetamine", ("Meth", "Crystal"), True)


class Cigarette(Narcotic):
    def __init__(self):
        super().__init__("Cigarette", ("Cig", "Fag"), False)