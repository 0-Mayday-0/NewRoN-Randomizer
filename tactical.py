from abstracts import Headwear, Long_Tactical, Grenade, Deployable

class Flashbang(Grenade):
    def __init__(self, name = "Flashbang"):
        super().__init__(name)

# noinspection PyPep8Naming
class CS_Gas(Grenade):
    def __init__(self, name = "CS Gas"):
        super().__init__(name)

class Stinger(Grenade):
    def __init__(self, name = "Stinger Grenade"):
        super().__init__(name)


# noinspection PyPep8Naming
class C2_Explosives(Deployable):
    def __init__(self, name: str = "C2 Explosives") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Door_Wedge(Deployable):
    def __init__(self, name: str = "Door Wedge") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Pepper_Spray(Deployable):
    def __init__(self, name: str = "Pepper Spray") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Lockpick_Gun(Deployable):
    def __init__(self, name: str = "Lockpick Gun") -> None:
        super().__init__(name)

# noinspection PyPep8Naming
class Mirror_Gun(Long_Tactical):
    def __init__(self, name: str = "Mirror Gun"):
        super().__init__(name)

# noinspection PyPep8Naming
class Breaching_Shotgun(Long_Tactical):
    def __init__(self, name: str = "Breaching Shotgun"):
        super().__init__(name)

# noinspection PyPep8Naming
class Ballistic_Shield(Long_Tactical):
    def __init__(self, name: str = "Ballistic Shield"):
        super().__init__(name)

# noinspection PyPep8Naming
class Rescue_Shield(Long_Tactical):
    def __init__(self, name: str = "Rescue Shield"):
        super().__init__(name)

# noinspection PyPep8Naming
class Battering_Ram(Long_Tactical):
    def __init__(self, name: str = "Battering Ram"):
        super().__init__(name)

# noinspection PyPep8Naming
class M320_Flash(Long_Tactical):
    def __init__(self, name: str = "M320 with Flashbang"):
        super().__init__(name)

# noinspection PyPep8Naming
class M320_Sting(Long_Tactical):
    def __init__(self, name: str = "M320 with Stinger"):
        super().__init__(name)

# noinspection PyPep8Naming
class M320_Gas(Long_Tactical):
    def __init__(self, name: str = "M320 with Gas"):
        super().__init__(name)


# noinspection PyPep8Naming
class No_Headwear(Headwear):
    def __init__(self, name: str = "No Headwear"):
        super().__init__(name)

# noinspection PyPep8Naming
class NVGS(Headwear):
    def __init__(self, name: str = "NVGS"):
        super().__init__(name)

# noinspection PyPep8Naming
class Anti_Flash_Goggles(Headwear):
    def __init__(self, name: str = "Anti-Flash Goggles"):
        super().__init__(name)

# noinspection PyPep8Naming
class CBRN_Riot_Mask(Headwear):
    def __init__(self, name: str = "CBRN Riot Gas Mask"):
        super().__init__(name)

# noinspection PyPep8Naming
class Ballistic_Facemask(Headwear):
    def __init__(self, name: str = "Ballistic Facemask"):
        super().__init__(name)