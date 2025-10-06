from heritage import *
from abstracts import *
from random import choice

###########AMMO###########

class AP(Ammo):
    def __init__(self, name="AP") -> None:
        super().__init__(name)

class JHP(Ammo):
    def __init__(self, name="JHP") -> None:
        super().__init__(name)

class Buckshot(Ammo):
    def __init__(self, name="Buckshot") -> None:
        super().__init__(name)

class Slug(Ammo):
    def __init__(self, name="Slug") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Flash_Shell(Ammo):
    def __init__(self, name="Flash Shell") -> None:
        super().__init__(name)

class Beanbag(Ammo):
    def __init__(self, name="Beanbag"):
        super().__init__(name)

class Pepperball(Ammo):
    def __init__(self, name="Pepperball") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Taser_Cartridge(Ammo):
    def __init__(self, name="Taser Cartridge") -> None:
        super().__init__(name)

###########!AMMO###########


###########OPTICS###########

# noinspection PyPep8Naming
class No_Optic(Optic):
    def __init__(self):
        super().__init__(name="None")

class SRS(Optic):
    def __init__(self, name = "SRS"):
        super().__init__(name)

# noinspection PyPep8Naming
class Holosight_EXPS3(Optic):
    def __init__(self, name = "Holosight EXPS3"):
        super().__init__(name)

class Microt2(Optic):
    def __init__(self, name = "Microt2"):
        super().__init__(name)

class M5B(Optic):
    def __init__(self, name = "M5B"):
        super().__init__(name)

# noinspection PyPep8Naming
class SDR_1_4x(Optic):
    def __init__(self, name = "SDR 1-4x"):
        super().__init__(name)

# noinspection PyPep8Naming
class SRO_Dot(Optic):
    def __init__(self, name = "SRO Dot"):
        super().__init__(name)

# noinspection PyPep8Naming
class RMR_Dot(Optic):
    def __init__(self, name = "RMR Dot"):
        super().__init__(name)

# noinspection PyPep8Naming
class Atak_R_1_12x(Optic):
    def __init__(self, name = "Atak-R 1-12x"):
        super().__init__(name)

class C510(Optic):
    def __init__(self, name = "510C"):
        super().__init__(name)

# noinspection PyPep8Naming
class XE_Sight(Optic):
    def __init__(self, name = "XE Sight"):
        super().__init__(name)

##########!OPTICS##################

##########MUZZLES##################

# noinspection PyPep8Naming
class No_Muzzle(Muzzle):
    def __init__(self):
        super().__init__(name="None")

# noinspection PyPep8Naming
class XF_brake(Muzzle):
    def __init__(self, name = "XF brake"):
        super().__init__(name)

class SnubNose(Muzzle):
    def __init__(self, name = "Snubnose"):
        super().__init__(name)

class Compensator(Muzzle):
    def __init__(self, name = "Compensator"):
        super().__init__(name)

# noinspection PyPep8Naming
class Spread_Choke(Muzzle):
    def __init__(self, name = "Spread Choke"):
        super().__init__(name)

# noinspection PyPep8Naming
class GA12_Brake(Muzzle):
    def __init__(self, name = "12GA Brake"):
        super().__init__(name)

# noinspection PyPep8Naming
class Socom_Suppressor(Muzzle):
    def __init__(self, name = "Socom Suppressor"):
        super().__init__(name)

# noinspection PyPep8Naming
class ASR_Brake(Muzzle):
    def __init__(self, name = "ASR Brake"):
        super().__init__(name)

# noinspection PyPep8Naming
class SFMB_Brake(Muzzle):
    def __init__(self, name = "SFMB Brake"):
        super().__init__(name)

# noinspection PyPep8Naming
class Harvester_Suppressor(Muzzle):
    def __init__(self, name = "Harvester Suppressor"):
        super().__init__(name)

# noinspection PyPep8Naming
class Tundra_Suppressor(Muzzle):
    def __init__(self, name = "Tundra Suppressor"):
        super().__init__(name)

class Suppressor(Muzzle):
    def __init__(self, name = "Suppressor"):
        super().__init__(name)

# noinspection PyPep8Naming
class MP9_Suppressor(Muzzle):
    def __init__(self, name = "MP9 Suppressor"):
        super().__init__(name)

# noinspection PyPep8Naming
class PBS_1_Suppressor(Muzzle):
    def __init__(self, name = "PBS-1 Suppressor"):
        super().__init__(name)

# noinspection PyPep8Naming
class Large_Suppressor(Muzzle):
    def __init__(self, name = "Large Suppressor"):
        super().__init__(name)

##########!MUZZLES##################


##########OVERBARREL##################

# noinspection PyPep8Naming
class No_Overbarrel(Overbarrel):
    def __init__(self):
        super().__init__(name="None")

# noinspection PyPep8Naming
class IR_Laser(Overbarrel):
    def __init__(self, name = "IR Laser"):
        super().__init__(name)


# noinspection PyPep8Naming
class Integrated_Flashlight(Overbarrel):
    def __init__(self, name = "Integrated Flashlight"):
        super().__init__(name)

# noinspection PyPep8Naming
class Laser_Pointer(Overbarrel):
    def __init__(self, name = "Laser Pointer"):
        super().__init__(name)

# noinspection PyPep8Naming
class Mault_IR_Laser(Overbarrel):
    def __init__(self, name = "Mault IR Laser"):
        super().__init__(name)

# noinspection PyPep8Naming
class PEQ_15_IR_Laser(Overbarrel):
    def __init__(self, name = "PEQ 15 IR Laser"):
        super().__init__(name)

# noinspection PyPep8Naming
class M600V_Flashlight(Overbarrel):
    def __init__(self, name = "M600V Flashlight"):
        super().__init__(name)

class Flashlight(Overbarrel):
    def __init__(self, name = "Flashlight"):
        super().__init__(name)

##########!OVERBARREL##################

##########UNDERBARREL##################

# noinspection PyPep8Naming
class No_Underbarrel(Underbarrel):
    def __init__(self, name = "None"):
        super().__init__(name)

# noinspection PyPep8Naming
class Angled_Grip(Underbarrel):
    def __init__(self, name = "Angled Grip"):
        super().__init__(name)

# noinspection PyPep8Naming
class Combat_Grip(Underbarrel):
    def __init__(self, name = "Combat Grip"):
        super().__init__(name)

# noinspection PyPep8Naming
class Vertical_Grip(Underbarrel):
    def __init__(self, name = "Vertical Grip"):
        super().__init__(name)

# noinspection PyPep8Naming
class Side_Angle_Grip(Underbarrel):
    def __init__(self, name: str = "Side Angle Grip"):
        super().__init__(name)

##########!UNDERBARREL##################

##########MAGAZINE##################

# noinspection PyPep8Naming
class Normal_Mag(Magazine):
    def __init__(self, name = "Normal Mag"):
        super().__init__(name)

# noinspection PyPep8Naming
class PMAG_5(Magazine):
    def __init__(self, name = "+5 PMAG"):
        super().__init__(name)


##########!MAGAZINE##################

##########STOCK##################

# noinspection PyPep8Naming
class Folded_Stock(Stock):
    def __init__(self, name = "Folded Stock"):
        super().__init__(name)

# noinspection PyPep8Naming
class Unfolded_Stock(Stock):
    def __init__(self, name = "Unfolded Stock"):
        super().__init__(name)

##########!STOCK##################

##########BASE GUNS###############
class Shotgun(Primary):
    def __init__(self, name):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   SRO_Dot(),
                                   RMR_Dot(),
                                   Microt2()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     GA12_Brake(),
                                     Spread_Choke()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             M600V_Flashlight(),
                                             Laser_Pointer()]

        self.ammo: list[Ammo] = [Buckshot(),
                                 Slug()]

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment]] = [self.optic,
                                        self.muzzle,
                                        self.overbarrel,
                                        self.ammo]

        return [choice(i) for i in pack]

# noinspection PyPep8Naming
class Assault_Rifle(Primary):
    def __init__(self, name):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Microt2(),
                                   SRS(),
                                   RMR_Dot(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Socom_Suppressor(),
                                     ASR_Brake(),
                                     SFMB_Brake()]

        self.underbarrel: list[Underbarrel] = [No_Underbarrel(),
                                               Vertical_Grip(),
                                               Angled_Grip(),
                                               Combat_Grip()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             M600V_Flashlight(),
                                             PEQ_15_IR_Laser()]

        self.ammo: list[Ammo] = [AP(),
                                 JHP()]

        self.magazine: list[Magazine] | None = None

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment | Ammo]] = [self.optic,
                                               self.muzzle,
                                               self.underbarrel,
                                               self.overbarrel,
                                               self.ammo]

        if self.magazine:
            pack.append(self.magazine)

        return [choice(i) for i in pack]


# noinspection PyPep8Naming
class SMG(Primary):
    def __init__(self, name):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   Microt2(),
                                   RMR_Dot(),
                                   SRO_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Tundra_Suppressor(),
                                     Harvester_Suppressor()]

        self.ammo: list[Ammo] = [AP(),
                                 JHP()]

        self.underbarrel: list[Underbarrel] | None = None
        self.overbarrel: list[Overbarrel] | None = None
        self.stock: list[Stock] | None = None

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment | Ammo]] = [self.optic,
                                               self.muzzle]

        if self.underbarrel:
            pack.append(self.underbarrel)

        if self.overbarrel:
            pack.append(self.overbarrel)

        if self.stock:
            pack.append(self.stock)

        pack.append(self.ammo)

        return [choice(i) for i in pack]

# noinspection PyPep8Naming
class Less_Lethal(Primary):
    def __init__(self, name):
        super().__init__(name)

        self.optic: list[Optic] = [No_Optic(),
                                   RMR_Dot(),
                                   SRO_Dot(),
                                   Microt2()]

        self.overbarrel: list[Overbarrel] = [No_Overbarrel(),
                                             Laser_Pointer(),
                                             Flashlight()]



        self.ammo: list[Ammo] | None = None

        self.underbarrel: list[Underbarrel] | None = None

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment | Ammo]] = [self.optic,
                                               self.overbarrel]

        if self.underbarrel:
            pack.append(self.underbarrel)

        pack.append(self.ammo)

        return [choice(i) for i in pack]

# noinspection PyPep8Naming
class Secondary_Less_Lethal(Secondary):
    def __init__(self, name):
        super().__init__(name)

        self.ammo: list[Ammo] = [Taser_Cartridge()]

    def random_attachments(self) -> list[Ammo]:
        pack: list[list[Ammo]] = [self.ammo]


        return [choice(i) for i in pack]

class Pistol(Secondary):
    def __init__(self, name):
        super().__init__(name)

        self.optic: list[Optic] | None = [No_Optic(),
                                          SRO_Dot(),
                                          RMR_Dot()]

        self.muzzle: list[Muzzle] = [No_Muzzle(),
                                     Compensator(),
                                     Large_Suppressor()]

        self.overbarrel: list[Overbarrel] | None = [No_Overbarrel(),
                                                    Flashlight(),
                                                    Laser_Pointer(),
                                                    IR_Laser()]

        self.ammo: list[Ammo] = [AP(),
                                 JHP()]

    def random_attachments(self) -> list[Attachment]:
        pack: list[list[Attachment | Ammo]] = [self.overbarrel,
                                               self.muzzle]

        if self.optic:
            pack.append(self.optic)

        pack.append(self.ammo)

        return [choice(i) for i in pack]

##########!BASE GUNS###############