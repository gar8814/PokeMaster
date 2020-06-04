#Define Pokemon Class that defines a pokemon by type and level
class Pokemon:
    def __init__(self, name, level, pType, koStatus = False):
        self.name = name
        self.level = level
        self.pType = pType
        self.max_health = level * 4 + 100
        self.curr_health = self.max_health
        self.KO = koStatus
    
    # method for taking damage
    def lose_health(self, damage):
        self.curr_health -= damage
        print("{name} has lost {damage} health; current health is {hp} hit points".format(name=self.name, damage=damage, hp=self.curr_health))
    
    #method for gaining HP
    def gain_health(self, healing):
        self.curr_health += healing
        print("{name} has gained {healing} points of healt".format(name=self.name, healing=healing))

    #method for Knocking Out a pokemon
    def knock_out(self):
        self.KO = True

    #method for reviving a pokemon from a KO
    def revive(self):
        self.KO = False

    #Attack a pokemon. Argument is a pokemon object
    def attack(self, other_pokemon):
        damage = 10 * self.level
        if self.pType == 'Fire':
            if other_pokemon.pType == 'Water':
                damage /= 2
            elif other_pokemon.pType == 'Grass':
                damage *= 2
                     


pikachu = Pokemon("Pikachu", 2, "Electic")
print(pikachu.max_health)
print(pikachu.curr_health)


