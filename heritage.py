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
        self.slots: int = 4
        self.deployable_slots: int = 2
        self.materials: list[Material] = [Kevlar(),
                                          Steel(),
                                          Ceramic()]

        self.sides: list[Side] = [No_Armor(),
                                  Front_Only(),
                                  Front_And_Back()]

        self.grenades: list[Grenade] = [Flashbang(),
                                        CS_Gas(),
                                        Stinger()]

        self.deployables: list[Deployable] = [C2_Explosives(),
                                              Door_Wedge(),
                                              Pepper_Spray(),
                                              Lockpick_Gun()]

    def random_setup(self) -> tuple[list[Material | Side],
                                    dict[Grenade, int],
                                    dict[Deployable, int]]:

        pack: list[list[Material] | list[Side] | list[Grenade]] = [self.materials]

        if self.sides:
            pack.append(self.sides)

        for i in range(self.slots):
            choice(self.grenades).add_one()

        for j in range(self.deployable_slots):
            choice(self.deployables).add_one()

        return ([choice(i) for i in pack],
                {g: g.quantity for g in self.grenades},
                {d: d.quantity for d in self.deployables})



    def pretty_print_setup(self) -> None:
        chosen: tuple[list[Material | Side], 
                      dict[Grenade, int],
                      dict[Deployable, int]] = self.random_setup()

        print(f'{re.search(r"(Armor)", str(self.__class__.__mro__[1])).group()}: {str(self)}')

        for i in chosen[0]:
            print(f'{re.search(r"(Material)|(Side)" ,str(i.__class__.__mro__[1])).group()}: {i}')
        print()

        for k, v in chosen[1].items():
            print(f'{k}: {v}')

        print()

        for k, v in chosen[2].items():
            print(f'{k}: {v}')


def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()