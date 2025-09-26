from abstracts import *
from random import choice
from abc import abstractmethod

class Primary(Gun):
    def __init__(self, name) -> None:
        super().__init__(name)

        self.optic: list[Optic] = []
        self.underbarrel: list[Underbarrel] = []
        self.overbarrel: list[Overbarrel] = []
        self.muzzle: list[Muzzle] = []
        self.magazine: list[Magazine] = []

    @abstractmethod
    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment] | list[None]] = [
                                            self.optic,
                                            self.underbarrel,
                                            self.overbarrel,
                                            self.muzzle,
                                            self.magazine
        ]

        return [choice(i) for i in pack]

    def pretty_print_attachments(self):
        chosen = self.random_attachments()

        print(f'{repr(self)}:\n')

        for i in chosen:
            print(i)

class Secondary(Gun):
    def __init__(self, name) -> None:
        super().__init__(name)

        self.optic: list[Optic] = []
        self.muzzle: list[Muzzle] = []
        self.underbarrel: list[Underbarrel] = []

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