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

##########!SHOTGUNS##################

##########ARs##################

# noinspection PyPep8Naming
class ARN_18(Assault_Rifle):
    def __init__(self, name = "ARN-18"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRS(),
                                   Holosight_EXPS3(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Mault_IR_Laser(),
                                             Laser_Pointer(),
                                             M600V_Flashlight()]


class ARWC(Assault_Rifle):
    def __init__(self, name = "ARWC"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]

# noinspection PyPep8Naming
class MK1_Carbine(Assault_Rifle):
    def __init__(self, name = "MK1 Carbine"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Combat_Grip()]

class G36C(Assault_Rifle):
    def __init__(self, name = "G36C"):
        super().__init__(name)

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Mault_IR_Laser(),
                                             Laser_Pointer(),
                                             M600V_Flashlight()]



class GA416(Assault_Rifle):
    def __init__(self, name = "GA416"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]


class M4A1(Assault_Rifle):
    def __init__(self, name = "M4A1"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x()]

        self.magazine: list[Magazine] = [Normal_Mag(),
                                         PMAG_5()]

# noinspection PyPep8Naming
class SA_58(Assault_Rifle):
    def __init__(self, name = "SA-58"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]

class MK16(Assault_Rifle):
    def __init__(self, name = "MK16"):
        super().__init__(name)
        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                               M600V_Flashlight(),
                                               Laser_Pointer(),
                                               Mault_IR_Laser()]

class SLR47(Assault_Rifle):
    def __init__(self, name = "SLR47"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   RMR_Dot(),
                                   Microt2(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     PBS_1_Suppressor()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Combat_Grip(),
                                               Angled_Grip()]
# noinspection PyPep8Naming
class SR_16(Assault_Rifle):
    def __init__(self, name = "SR-16"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x(),
                                   Atak_R_1_12x()]



##########!ARs##################

def main():
    SR_16().pretty_print_attachments()

if __name__ == '__main__':
    main()