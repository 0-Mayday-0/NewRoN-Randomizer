from heritage import *
from abstracts import *


###########OPTICS###########
class SRS(Optic):
    def __init__(self, name = "SRS"):
        super().__init__(name)

class Holosight_EXPS3(Optic):
    def __init__(self, name = "Holosight EXPS3"):
        super().__init__(name)

class Microt2(Optic):
    def __init__(self, name = "Microt2"):
        super().__init__(name)

class M5B(Optic):
    def __init__(self, name = "M5B"):
        super().__init__(name)

class SDR_1_4x(Optic):
    def __init__(self, name = "SDR 1-4x"):
        super().__init__(name)
##########OPTICS##################

##########BASE GUNS###############
class BasePrimary(Primary):
    def __init__(self, name, allows_muzzle: bool = True, allows_magazine: bool = False):
        super().__init__(name)

        self.allows_muzzle = allows_muzzle
        self.allows_magazine = allows_magazine

        self.optic: list[Optic] = [SRS(),
                                   Holosight_EXPS3(),
                                   Microt2(),
                                   M5B(),
                                   SDR_1_4x()]

##########BASE GUNS###############