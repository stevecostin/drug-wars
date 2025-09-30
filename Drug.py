class Drug:
    def __init__(self) -> None:
        self.price = 0
        self.possess_num_of_grams = 0

    def set_price_per_gram(self, price: int) -> None:
        self.price = price

    def get_price_per_gram(self) -> int:
        return self.price

    def add_drug_to_possession(self, num_of_grams: int) -> None:
        self.possess_num_of_grams += num_of_grams

    def remove_drug_from_possession(self, num_of_grams: int) -> None:
        self.possess_num_of_grams -= num_of_grams

    def get_drug_possession(self) -> int:
        return self.possess_num_of_grams


class Weed(Drug):
    long_name: str = "Marijuana"
    short_name: str = ("Weed", "Ganja")

    @classmethod
    def get_long_name(cls) -> str:
        return cls.long_name

    @classmethod
    def get_short_name(cls) -> str:
        pass


class Cocaine(Drug):
    long_name: str = "Cocaine"
    short_name: str = ("Coke",)

    @classmethod
    def get_long_name(cls) -> str:
        return cls.long_name

    @classmethod
    def get_short_name(cls) -> str:
        pass