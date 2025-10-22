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

        self.optic.remove(Holosight_EXPS3())
        self.optic.remove(C510())
        self.optic.remove(XE_Sight())

# noinspection PyPep8Naming
class CQB_870(Shotgun):
    def __init__(self, name = "870 CQB"):
        super().__init__(name)

        self.optic.remove(Holosight_EXPS3())
        self.optic.remove(C510())
        self.optic.remove(XE_Sight())

        self.overbarrel.remove(M600V_Flashlight())
        self.overbarrel.append(Integrated_Flashlight())


class M590(Shotgun):
    def __init__(self, name = "590M"):
        super().__init__(name)


class M1014(Shotgun):
    def __init__(self, name = "M1014"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRO_Dot(),
                                   RMR_Dot()]

class Supernova(Shotgun):
    def __init__(self, name = "Supernova"):
        super().__init__(name)



##########!SHOTGUNS##################

##########ARs##################

# noinspection PyPep8Naming
class ARN_18(Assault_Rifle):
    def __init__(self, name = "ARN-180"):
        super().__init__(name)

        self.optic.remove(Atak_R_1_12x())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())


class ARWC(Assault_Rifle):
    def __init__(self, name = "ARWC"):
        super().__init__(name)




class G36C(Assault_Rifle):
    def __init__(self, name = "G36C"):
        super().__init__(name)

        self.optic: list[Optic] = [RMR_Dot(),
                                   SRO_Dot(),
                                   Microt2()]

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())



class GA416(Assault_Rifle):
    def __init__(self, name = "GA416"):
        super().__init__(name)


# noinspection PyPep8Naming
class SA_58(Assault_Rifle):
    def __init__(self, name = "SA-58 OSW"):
        super().__init__(name)

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())


class MK16(Assault_Rifle):
    def __init__(self, name = "MK16"):
        super().__init__(name)

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())


class SLR47(Assault_Rifle):
    def __init__(self, name = "SLR47"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   RMR_Dot(),
                                   Microt2(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     PBS_1_Suppressor()]

        self.underbarrel.remove(Vertical_Grip())


# noinspection PyPep8Naming
class SR_16(Assault_Rifle):
    def __init__(self, name = "SR-16"):
        super().__init__(name)



# noinspection PyPep8Naming
class DM4PDW(Assault_Rifle):
    def __init__(self, name = "DM4PDW"):
        super().__init__(name)

        self.optic.remove(Atak_R_1_12x())

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Socom_Suppressor()]

        self.underbarrel.append(Side_Angle_Grip())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())

class F90(Assault_Rifle):
    def __init__(self, name = "F90"):
        super().__init__(name)

        self.underbarrel.remove(Angled_Grip())
        self.underbarrel.append(Side_Angle_Grip())

        self.overbarrel.append(Mault_IR_Laser())

class G3A3(Assault_Rifle):
    def __init__(self, name = "G3A3"):
        super().__init__(name)

        self.muzzle.remove(Socom_Suppressor())
        self.muzzle.append(Tundra_Suppressor())

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

class GA51(Assault_Rifle):
    def __init__(self, name = "GA51"):
        super().__init__(name)

        self.optic.remove(SDR_1_4x())
        self.optic.remove(Atak_R_1_12x())
        self.optic.append(RMR_Dot())
        self.optic.append(SRO_Dot())

        self.muzzle.remove(Socom_Suppressor())
        self.muzzle.append(Tundra_Suppressor())

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

class LVAR(Assault_Rifle):
    def __init__(self, name = "LVAR"):
        super().__init__(name)

        self.muzzle = None

        self.underbarrel.append(Side_Angle_Grip())

        self.overbarrel.append(Mault_IR_Laser())
        self.overbarrel.append(WM_Light())

# noinspection PyPep8Naming
class M14S_16(Assault_Rifle):
    def __init__(self, name = "M14S-16"):
        super().__init__(name)

        self.underbarrel = None

        self.optic.append(AimPro())

        self.muzzle.remove(ASR_Brake())
        self.muzzle.remove(SFMB_Brake())

class MCX(Assault_Rifle):
    def __init__(self, name = "MCX"):
        super().__init__(name)

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())
        self.overbarrel.append(WM_Light())

class MK17(Assault_Rifle):
    def __init__(self, name = "MK17"):
        super().__init__(name)

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

        self.overbarrel.append(PEQ_15_IR_Laser())

class MK18(Assault_Rifle):
    def __init__(self, name = "MK18"):
        super().__init__(name)

        self.optic.remove(Atak_R_1_12x())

        self.underbarrel.append(Side_Angle_Grip())
        self.underbarrel.append(TH_Grip())

##########!ARs##################

##########SMGs##################

# noinspection PyPep8Naming
class MP5_10mm(SMG):
    def __init__(self, name = "MP5/10mm"):
        super().__init__(name)


# noinspection PyPep8Naming
class MP5A3(SMG):
    def __init__(self, name = "MP5A3"):
        super().__init__(name)


# noinspection PyPep8Naming
class MP5A2(SMG):
    def __init__(self, name = "MP5A2"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRO(),
                                   MicroSight(),
                                   EXPS3()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Suppressor()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Flashlight()]

# noinspection PyPep8Naming
class MP9(SMG):
    def __init__(self, name = "MP9"):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRO_Dot(),
                                   RMR_Dot(),
                                   Microt2()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     MP9_Suppressor()]

        self.overbarrel.append(Mault_IR_Laser())

        self.underbarrel: list[Underbarrel] | None = None

# noinspection PyPep8Naming
class MPX(SMG):
    def __init__(self, name = "MPX"):
        super().__init__(name)

        self.optic.remove(RMR_Dot())
        self.optic.remove(AimPro())

        self.overbarrel.remove(PEQ_15_IR_Laser())
        self.overbarrel.append(Mault_IR_Laser())


# noinspection PyPep8Naming
class UMP_45(SMG):
    def __init__(self, name = "UMP-45"):
        super().__init__(name)

        self.optic.remove(RMR_Dot())
        self.optic.remove(AimPro())
        self.optic.append(SRS())

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Suppressor()]

##########!SMGs##################

##########LESSLETHAL##################

# noinspection PyPep8Naming
class Beanbag_Shotgun(Less_Lethal):
    def __init__(self, name="Beanbag Shotgun"):
        super().__init__(name)
        self.optic: list[Optic] = [No_Optic(),
                                   RMR_Dot(),
                                   SRO_Dot(),
                                   Microt2()]

        self.underbarrel: list[Underbarrel] | None = None

        self.overbarrel.remove(M600V_Flashlight())
        self.overbarrel.remove(Mault_IR_Laser())
        self.overbarrel.append(Flashlight())

        self.ammo: list[Ammo] = [Beanbag()]

# noinspection PyPep8Naming
class VPL_25(Less_Lethal):
    def __init__(self, name="VPL-25"):
        super().__init__(name)

        self.ammo: list[Ammo] = [Pepperball()]

class TRPL(Secondary_Less_Lethal):
    def __init__(self, name="TRPL"):
        super().__init__(name)

##########!LESSLETHAL##################

##########PISTOLS#################

class B92X(Pistol):
    def __init__(self, name="B92X"):
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
    def __init__(self, name="Five-Seven"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Tundra_Suppressor()]

class M45A1(Pistol):
    def __init__(self, name="M45A1"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Compensator(),
                                     Obsidian_Supressor()]


class G19(Pistol):
    def __init__(self, name="Glock-19"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Compensator(),
                                     GM_Supressor()]

# noinspection PyPep8Naming
class USP45(Pistol):
    def __init__(self, name="USP45"):
        super().__init__(name)

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Suppressor(),
                                     Obsidian_Supressor()]

# noinspection PyPep8Naming
class Sig_509(Pistol):
    def __init__(self, name="509"):
        super().__init__(name)

        self.muzzle.remove(XF_brake())

# noinspection PyPep8Naming
class M11_Compact(Pistol):
    def __init__(self, name="M11 Compact"):
        super().__init__(name)

        self.muzzle: list[Muzzle] | None = None

# noinspection PyPep8Naming
class MK_V(Pistol):
    def __init__(self, name="MK-V"):
        super().__init__(name)

        self.optic: list[Optic] | None = None
        self.muzzle: list[Muzzle] | None = None

        self.overbarrel.remove(Flashlight())
        self.overbarrel.remove(IR_Laser())
        self.overbarrel.append(Custom_Laser())

# noinspection PyPep8Naming
class TLE_1911(Pistol):
    def __init__(self, name="TLE 1911"):
        super().__init__(name)

        self.muzzle: list[Muzzle] | None = None

        self.overbarrel.remove(IR_Laser())

##########!PISTOLS#################

def main():
    Supernova().pretty_print_attachments()
    Anti_Stab_Vest().pretty_print_setup()

if __name__ == '__main__':
    main()