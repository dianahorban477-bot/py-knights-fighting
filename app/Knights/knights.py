class Knights:
    def __init__(self, data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = data["armour"]
        self.weapon = data["weapon"]
        self.potion = data["potion"]
        self.protection = 0

    def prepare_for_battle(self):
        for arm in self.armour:
            self.protection += arm["protection"]

        self.power += self.weapon["power"]
        if self.potion:
            self.protection +=\
                self.potion["effect"].get("protection", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)


def battle(knight1, knight2):
    damage_to_k1 = max(0, knight2.power - knight1.protection)
    damage_to_k2 = max(0, knight1.power - knight2.protection)
    knight1.hp = max(0, knight1.hp - damage_to_k1)
    knight2.hp = max(0, knight2.hp - damage_to_k2)
