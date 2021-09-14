from random import choice


class Unit:
    created_units_counter = 0
    #          hero       skill              ability
    heroes = {'Mage': ['Intelligence', ['Air', 'Fire', 'Water']],
              'Archer': ['Agility', ['Bow', 'Crossbow', 'Prashcha']],
              'Knight': ['Strength', ['Sword', 'Axe', 'Pike']]
              }

    def __init__(self, name, clan):
        self._name = name
        self.clan = clan
        self._health = 100
        self._Strength = 1
        self._Intelligence = 1
        self._Agility = 1
        Unit.created_units_counter += 1

    def __str__(self):
        return f"Hello, {self.clan} {self._name}!\n" \
               f"You are created with:\nHealth: {self._health}%" \
               f", Strength {self._Strength}, Agility {self._Agility}," \
               f" Intelligence {self._Intelligence}\n"

    def increase_health(self):
        if self._health <= 90:
            self._health += 10
        else:
            self._health = 100

    def check_info(self):
        return f"Health: {self._health}%" \
               f", Strength {self._Strength}, Agility {self._Agility}," \
               f" Intelligence {self._Intelligence}\n" \
               f"There are {self.created_units_counter} Heroes online\n" \
               f"-------------------\n"


class Hero(Unit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.skill = Unit.heroes[self.clan][0]
        self.mage_type = choice(Unit.heroes[self.clan][1])

    def __str__(self):
        return f"{super().__str__()}You have great '{self.skill}'" \
               f" and weapon is: {self.mage_type}\n" \
               f"-------------------\n"

    def skill_up(self):
        exec(f'self._{self.skill} += 1')
