class Character(object):

    def __init__(self, name, race, level, health, stamina, defence, skill, status):
        self.name = name
        self.race = race
        self.level = level
        self.health = health
        self.stamina = stamina
        self.defence = defence
        self.skill = skill
        self.status = status

    def level_up(self):
        level += 1
        health += ((299*(level - 1))/39) + 1
        stamina += ((99*(level - 1))/39) + 1
        defense += ((99*(level - 1))/39) + 1

    @property
    def is_dead(self):
        return self.health == 0

    @property
    def is_tired(self):
        return self.stamina == 0

    @property
    def is_poisoned(self):
        return self.status = "poison"



class Monster(Character):
    def __init__(self, name, race, level, health, stamina, defence, skill):
        Character.__init__(self, name, race, level, health, stamina, defence, skill)
        
class Item(object):
    
    def __init__(self, name, effect, requirements):
        self.name = name
        self.effect = effect
        self.requirements = requirements 
        
class Weapon(Item):

    def __init__(self, name, effect, requirements, damage):
        Item.__init__(self, name, effect, requirements)
        self.damage = damage



