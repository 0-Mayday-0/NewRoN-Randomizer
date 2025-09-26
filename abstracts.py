from abc import ABC, abstractmethod

class Attachment(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self.name: str = name


    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}"

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


def main():
    at = [Optic("Red dot"), Underbarrel("Flash")]

    for i in at:
        print(repr(i))


if __name__ == '__main__':
    main()