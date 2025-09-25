from abstracts import *
from random import choice

class Primary(Gun):
    def __init__(self, name, allows_muzzle: bool = False, allows_magazine: bool = False) -> None:
        super().__init__(name)

        self.allows_muzzle: bool = allows_muzzle
        self.allows_magazine: bool  = allows_magazine

        self.optic: list[Optic] = []
        self.underbarrel: list[Underbarrel] = []
        self.overbarrel: list[Overbarrel] = []
        self.muzzle: list[Muzzle] = []
        self.magazine: list[Magazine] = []

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment]] = [self.optic,
                                        self.underbarrel,
                                        self.overbarrel]

        if self.allows_muzzle:
            pack.append(self.muzzle)
        if self.allows_magazine:
            pack.append(self.magazine)



        return [choice(i) for i in pack]

    def pretty_print_attachments(self):
        chosen = self.random_attachments()

        print(f'{repr(self)}:\n')

        for i in chosen:
            print(i)

class Secondary(Gun):
    def __init__(self, name, allows_optic: bool = True) -> None:
        super().__init__(name)

        self.allows_optic: bool = allows_optic

        self.optic: list[Optic] = []
        self.muzzle: list[Muzzle] = []
        self.underbarrel: list[Underbarrel] = []

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment]] = [self.muzzle,
                                        self.underbarrel]

        if self.allows_optic:
            pack.append(self.optic)

        return [choice(i) for i in pack]

    def pretty_print_attachments(self):
        print(f'{repr(self)}:\n')
        for i in self.random_attachments():
            print(i)

def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()