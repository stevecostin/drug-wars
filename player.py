from narcotic import Narcotic
from weapon import Weapon

class NarcoticManager:
    def __init__(self) -> None:
        self.narcotics = []

    def add_narcotic(self, narcotic: Narcotic):
        if narcotic in self.narcotics:
            pass
        else:
            self.narcotics.append(narcotic)

    def get_narcotics(self) -> tuple:
        return tuple(self.narcotics)

    def remove_narcotic(self, narcotic: Narcotic) -> None:
        pass


class WeaponManager:
    def __init__(self) -> None:
        self.weapons = []

    def add_weapon(self, weapon: Weapon) -> None:
        if weapon in self.weapons:
            pass
        else:
            self.weapons.append(weapon)

    def get_weapons(self) -> tuple:
        return tuple(self.weapons)

    def remove_weapon(self, weapon: Weapon) -> None:
        pass


class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.narcotic_manager = NarcoticManager()
        self.weapon_manager = WeaponManager()

    def __str__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_narcotic_manager(self) -> NarcoticManager:
        return self.narcotic_manager

    def get_weapon_manager(self) -> WeaponManager:
        return self.weapon_manager