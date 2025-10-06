from weapons import *

##########GEAR##################

# noinspection PyPep8Naming
class Anti_Stab_Vest(Armor):
    def __init__(self, name="Anti-Stab Vest") -> None:
        super().__init__(name)
        self.sides: None = None
        self.deployable_slots: int = 3

# noinspection PyPep8Naming
class Light_Armor(Armor):
    def __init__(self, name="Light Armor") -> None:
        super().__init__(name)
        self.slots: int = 3

# noinspection PyPep8Naming
class Heavy_Armor(Armor):
    def __init__(self, name="Heavy Armor") -> None:
        super().__init__(name)
        self.slots: int = 2

##########!GEAR##################

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

# noinspection PyPep8Naming
class DM4PDW(Assault_Rifle):
    def __init__(self, name = "DM4PDW"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRS(),
                                   Microt2(),
                                   M5B(),
                                   C510(),
                                   Holosight_EXPS3(),
                                   XE_Sight(),
                                   SDR_1_4x()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Combat_Grip(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Side_Angle_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Mault_IR_Laser(),
                                             M600V_Flashlight(),
                                             Laser_Pointer()]

##########!ARs##################

##########SMGs##################

# noinspection PyPep8Naming
class MP5_10mm(SMG):
    def __init__(self, name = "MP5/10mm"):
        super().__init__(name)

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Combat_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             M600V_Flashlight(),
                                             PEQ_15_IR_Laser()]

# noinspection PyPep8Naming
class MP5A3(SMG):
    def __init__(self, name = "MP5A3"):
        super().__init__(name)

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Combat_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             M600V_Flashlight(),
                                             PEQ_15_IR_Laser()]

# noinspection PyPep8Naming
class MP5A2(SMG):
    def __init__(self, name = "MP5A2"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Microt2(),
                                   SRS(),
                                   Holosight_EXPS3(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Suppressor()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Flashlight()]

# noinspection PyPep8Naming
class MP9(SMG):
    def __init__(self, name = "MP9"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     MP9_Suppressor()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             M600V_Flashlight(),
                                             Mault_IR_Laser(),
                                             Laser_Pointer()]

# noinspection PyPep8Naming
class MPX(SMG):
    def __init__(self, name = "MPX"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   Microt2(),
                                   SRO_Dot()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Combat_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             M600V_Flashlight(),
                                             Mault_IR_Laser(),
                                             Laser_Pointer()]


# noinspection PyPep8Naming
class UMP_45(SMG):
    def __init__(self, name = "UMP-45"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Microt2(),
                                   Holosight_EXPS3(),
                                   SRS(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Large_Suppressor()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Combat_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             M600V_Flashlight()]

        self.stock: list[Stock] = [Unfolded_Stock(),
                                   Folded_Stock()]
##########!SMGs##################

##########LESSLETHAL##################

# noinspection PyPep8Naming
class Beanbag_Shotgun(Less_Lethal):
    def __init__(self, name="Beanbag Shotgun"):
        super().__init__(name)
        self.ammo: list[Ammo] = [Beanbag()]

# noinspection PyPep8Naming
class R7_Launcher(Less_Lethal):
    def __init__(self, name="R7 Launcher"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Holosight_EXPS3(),
                                   Microt2(),
                                   M5B(),
                                   SRS()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Combat_Grip(),
                                               Angled_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             M600V_Flashlight(),
                                             Laser_Pointer(),
                                             Mault_IR_Laser()]

        self.ammo: list[Ammo] = [Pepperball()]

class Taser(Secondary_Less_Lethal):
    def __init__(self, name="Taser"):
        super().__init__(name)

##########!LESSLETHAL##################

##########PISTOLS#################

class P92X(Pistol):
    def __init__(self, name="P92X"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     XF_brake(),
                                     Suppressor()]

class Magnum357(Pistol):
    def __init__(self, name=".357 Magnum"):
        super().__init__(name)

        self.optic: list[Optic] | None = None

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     SnubNose()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer()]
# noinspection PyPep8Naming
class USG_57(Pistol):
    def __init__(self, name="57 USG"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Tundra_Suppressor()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             Flashlight()]

class M45A1(Pistol):
    def __init__(self, name="M45A1"):
        super().__init__(name)

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             Flashlight()]

class PC19(Pistol):
    def __init__(self, name="PC19"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Compensator(),
                                     Suppressor()]
# noinspection PyPep8Naming
class USP45(Pistol):
    def __init__(self, name="USP45"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Suppressor()]

##########!PISTOLS#################

def main():
    DM4PDW().pretty_print_attachments()
    Anti_Stab_Vest().pretty_print_setup()

if __name__ == '__main__':
    main()