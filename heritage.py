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

def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()