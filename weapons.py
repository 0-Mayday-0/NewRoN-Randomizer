from heritage import *
from abstracts import *


###########OPTICS###########

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

##########!OPTICS##################

##########MUZZLES##################

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

        self.optic: list[Optic] = [SRO_Dot(),
                                   RMR_Dot()]

    def random_attachments(self) -> list[Attachment]:
        raise NotImplementedError

##########!BASE GUNS###############