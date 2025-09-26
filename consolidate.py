from weapons import *

##########SHOTGUNS##################
class B1301(Shotgun):
    def __init__(self, name = "B1301"):
        super().__init__(name)

# noinspection PyPep8Naming
class CQB_870(Shotgun):
    def __init__(self, name = "870 CQB"):
        super().__init__(name)
        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Integrated_Flashlight(),
                                             Laser_Pointer()]

# noinspection PyPep8Naming
class Entryman(Shotgun):
    def __init__(self, name = "B1301 \"Entryman\""):
        super().__init__(name)

# noinspection PyPep8Naming
class M4_Super_90(Shotgun):
    def __init__(self, name = "M4 Super 90"):
        super().__init__(name)
        self.optic: list[Optic] = [No_Optic(),
                                   RMR_Dot(),
                                   SRO_Dot()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Flashlight(),
                                             Laser_Pointer()]

##########SHOTGUNS##################

def main():
    M4_Super_90().pretty_print_attachments()

if __name__ == '__main__':
    main()