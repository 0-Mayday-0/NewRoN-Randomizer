from consolidate import *
from tactical import *

class WeaponsPack:
    def __init__(self) -> None:
        self.shotguns: list[Shotgun] = [B1301(),
                                        CQB_870(),
                                        Entryman(),
                                        M4_Super_90()]

        self.ars: list[Assault_Rifle] = [ARN_18(),
                                         ARWC(),
                                         MK1_Carbine(),
                                         G36C(),
                                         GA416(),
                                         M4A1(),
                                         SA_58(),
                                         MK16(),
                                         SLR47(),
                                         SR_16()]

        self.smgs: list[SMG] = [MP5_10mm(),
                                MP5A3(),
                                MP5A2(),
                                MP9(),
                                MPX(),
                                UMP_45()]

        self.primary_ll: list[Less_Lethal] = [Beanbag_Shotgun(),
                                              R7_Launcher()]

        self.pistols: list[Pistol] = [P92X(),
                                      Magnum357(),
                                      USG_57(),
                                      M45A1(),
                                      PC19(),
                                      USP45()]

        self.secondary_ll: list[Secondary_Less_Lethal] = [Taser()]

        self.armor: list[Armor] = [Anti_Stab_Vest(),
                                   Light_Armor(),
                                   Heavy_Armor()]

        self.long_tactical: list[Long_Tactical] = [Mirror_Gun(),
                                                   Breaching_Shotgun(),
                                                   Ballistic_Shield(),
                                                   Rescue_Shield(),
                                                   Battering_Ram(),
                                                   M320_Flash(),
                                                   M320_Sting(),
                                                   M320_Gas()]

        self.headwear: list[Headwear] = [No_Headwear(),
                                         NVGS(),
                                         Anti_Flash_Goggles(),
                                         CBRN_Riot_Mask(),
                                         Ballistic_Facemask()]


    def randomize(self) -> None:
        primaries: list[Primary | Less_Lethal] = self.shotguns+self.ars+self.smgs+self.primary_ll

        secondaries: list[Secondary | Secondary_Less_Lethal] = self.pistols+self.secondary_ll

        long_tac: Long_Tactical = choice(self.long_tactical)
        headw: Headwear = choice(self.headwear)

        choice(primaries).pretty_print_attachments()
        print()
        choice(secondaries).pretty_print_attachments()

        print(f'\n{re.search(r"(Long_Tactical)", str(long_tac.__class__.__mro__[1])).group().replace('_', ' ')}: {str(long_tac)}')
        print(f'{re.search(r'(Headwear)', str(headw.__class__.__mro__[1])).group()}: {str(headw)}\n\n')

def main() -> None:
    wp = WeaponsPack()

    while True:
        wp.randomize()
        input()

if __name__ == '__main__':
    main()