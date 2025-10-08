from abc import ABC, abstractmethod
from random import choice

class Throwable(ABC):
    def __init__(self, name: str):
        self.name = name
        self.quantity: int = 0

    def __str__(self):
        return self.name

    @abstractmethod
    def add_one(self) -> None:
        pass

# noinspection PyPep8Naming
class Long_Tactical(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Headwear(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Tactical(ABC):
    def __init__(self, name: str):
        self.name = name
        self.quantity: int = 0

    def __str__(self):
        return self.name

    @abstractmethod
    def add_one(self) -> None:
        pass

class Side(ABC):
    def __init__(self, orientation: str):
        self.orientation = orientation

    def __str__(self):
        return self.orientation

class Material(ABC):
    def __init__(self, material: str):
        self.material = material

    def __str__(self):
        return self.material

class Gear(ABC):
    def __init__(self, name: str):
        self.name = name
        self.slots: int
        self.grenades: list[Throwable]
        self.sides: list[Side]
        self.materials: list[Material]

    def __str__(self):
        return self.name

    @abstractmethod
    def random_setup(self) -> list[Side | Material]:
        pass

class Ammo(ABC):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

class Attachment(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name


    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}"

    def __eq__(self, other):
        return self.name == other.name

class Kevlar(Material):
    def __init__(self, material: str = "Kevlar") -> None:
        super().__init__(material)

class Steel(Material):
    def __init__(self, material: str = "Steel") -> None:
        super().__init__(material)

class Ceramic(Material):
    def __init__(self, material: str = "Ceramic") -> None:
        super().__init__(material)

# noinspection PyPep8Naming
class No_Armor(Side):
    def __init__(self, orientation: str = "No armor") -> None:
        super().__init__(orientation)

# noinspection PyPep8Naming
class Front_Only(Side):
    def __init__(self, orientation: str = "Front only") -> None:
        super().__init__(orientation)

# noinspection PyPep8Naming
class Front_And_Back(Side):
    def __init__(self, orientation: str = "Front & Back") -> None:
        super().__init__(orientation)

class Optic(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Stock(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Underbarrel(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Overbarrel(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Muzzle(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Magazine(Attachment):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Gun(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name
        self.optic: list[Optic]
        self.underbarrel: list[Underbarrel]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}"

    @abstractmethod
    def random_attachments(self) -> list[Attachment]:
        pass

##########THROWABLES###############
class Grenade(Throwable):
    def __init__(self, name) -> None:
        super().__init__(name)

    def add_one(self) -> None:
        self.quantity += 1


##########!THROWABLES###############

##########TACTICAL###############

class Deployable(Tactical):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def add_one(self) -> None:
        self.quantity += 1


##########!TACTICAL###############

def main():
    at = [Optic("Red dot"), Underbarrel("Flash")]

    for i in at:
        print(repr(i))


if __name__ == '__main__':
    main()