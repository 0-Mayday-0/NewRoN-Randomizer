from abstracts import *
from random import choice
from abc import abstractmethod
import re

class Primary(Gun):
    def __init__(self, name) -> None:
        super().__init__(name)

        self.optic: list[Optic] = []
        self.underbarrel: list[Underbarrel] = []
        self.overbarrel: list[Overbarrel] = []
        self.muzzle: list[Muzzle] = []
        self.magazine: list[Magazine] = []
        self.ammo: list[Ammo] = []

    @abstractmethod
    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment] | list[None]] = [
                                            self.optic,
                                            self.underbarrel,
                                            self.overbarrel,
                                            self.muzzle,
                                            self.magazine,
                                            self.ammo
        ]

        return [choice(i) for i in pack]

    def pretty_print_attachments(self):
        chosen = self.random_attachments()
        pattern: re.Pattern = re.compile(r'(Optic)|(Underbarrel)|(Overbarrel)|(Muzzle)|(Magazine)|(Attachment)|(Ammo)')

        print(f'{str(self)}:\n')

        for i in chosen:
            print(f'{re.search(pattern, str(i.__class__.__mro__[1])).group()}: {i}')

class Secondary(Gun):
    def __init__(self, name) -> None:
        super().__init__(name)

        self.optic: list[Optic] = []
        self.muzzle: list[Muzzle] = []
        self.underbarrel: list[Underbarrel] = []
        self.ammo: list[Ammo] = []

    @abstractmethod
    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment]] = [self.muzzle,
                                        self.underbarrel,
                                        self.optic]


        return [choice(i) for i in pack]

    def pretty_print_attachments(self):
        print(f'{repr(self)}:\n')
        for i in self.random_attachments():
            print(i)

class Armor(Gear):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.materials: list[Material] = [Kevlar(),
                                          Steel(),
                                          Ceramic()]

        self.sides: list[Side] = [No_Armor(),
                                  Front_Only(),
                                  Front_And_Back()]

    def random_setup(self) -> list[Material | Side]:
        if self.sides:
            return [choice(i) for i in (self.materials, self.sides)]

        else:
            return [choice(self.materials)]

    def pretty_print_setup(self) -> None:
        chosen: list[Material | Side] = self.random_setup()

        print(f'{re.search(r"(Armor)", str(self.__class__.__mro__[1])).group()}: {str(self)}')

        for i in chosen:
            print(f'{re.search(r'(Material)|(Side)', str(i.__class__.__mro__[1])).group()}: {i}')

def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()