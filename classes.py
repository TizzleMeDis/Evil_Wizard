from character import *
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=30, defense=10, accuracy=75, agility=15, stunned=False, poisoned=False,
                            special_abilities={
                                1:"Rage - Attack: +20 | Accuracy: -10",
                                2:"Strike - Damage: 50 points",
                                3:"Fast Heal - Health: +20"
                            }, cooldown=0)  # Boost health and attack power
    def special_ability(self, special, opponent):
        if special == "1":
            self.accuracy -= 10
            self.attack_power += 20
            print("\nRAWWWWWRRRRR!!")
            super().display_stats()
        elif special == "2":
            self.attack_power += 20
            super().attack(opponent)
            self.attack_power -= 20
        else: #default ability
            print(f"{self.name} healed for 20 health points")
            self.health += 20
            if self.health > self.max_health:
                self.health = self.max_health
            super().display_stats()

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=45, defense=5, accuracy=65, agility=10, stunned=False, poisoned=False,
                            special_abilities={
                                1:"Stasis - Freeze Target|add accuracy: 25",
                                2:"Fire Ball - High Damage Spell - 75",
                                3:"Over heal + 100"
                            }, cooldown=0)  # Boost high damage spells
    def special_ability(self, special, opponent):
        if special == "1":
            print("\nFocusing.... FREEZE!!")
            self.accuracy += 40
            opponent.stunned = True
        elif special == "2":
            self.attack_power += 30
            super().attack(opponent)
            self.attack_power -= 30
        else: #default ability
            print(f"{self.name} healed all wounds")
            self.health += 100
            if self.health > self.max_health:
                self.health = self.max_health
            super().display_stats()
    # Add your cast spell method here

# Warrior class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=25, defense=7, accuracy=90, agility=35, stunned=False, poisoned=False,
                            special_abilities={
                                1:"Eagle Vision - improve accuracy 25",
                                2:"Evade - dodge next attack",
                                3:"Double Shot - attack twice"
                            }, cooldown=0)  # Boost Accuracy and stealth power
    
    def special_ability(self, special, opponent):
        if special == "1":
            print(f"\n{self.name} says, 'They call me DeadShot in some parts..'\n")
            self.accuracy += 25
        elif special == "2":
            print(f"\n'I move too quick...' says {self.name}")
            opponent.stunned = True
        else: #default ability
            print(f"\n{self.name} used Double Shot\n")
            super().attack(opponent)
            super().attack(opponent)

    # Add your power attack method here
    
# Warrior class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=300, attack_power=15, defense=15, accuracy=95, agility=10, stunned=False, poisoned=False,
                            special_abilities= {
                                1:"Fortify",
                                2:"Regenerate",
                                3:"Shield Bash"
                            }, cooldown=0)  # Boost Defense and Vitality
    
    def special_ability(self, special, opponent):
        if special == "1":
            print(f"\nA powerful force surrounds {self.name} | Defense Rose: +10\n")
            self.defense += 10
        elif special == "2":
            print(f"\n{self.name} drank a potion")
            self.health += 15  # Lower regeneration amount
            
        else: #default ability
            print(f"\n{self.name} used Shield Bash")
            super().attack(opponent)
            if super().hit_chance() > 50:
                print(f"{opponent.name} is stunned!\n")
                opponent.stunned = True
    # Add your power attack method here

# EvilWizard Class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=15, defense=10, accuracy=95, agility=10, stunned=False, poisoned=False,
                            special_abilities={
                                1:"Overcharge - Increase attack and Regeneration",
                                2:"Fire Ball - Attack for 30",
                                3:"Mind Rot - accuracy - 25"
                            }, cooldown=0)  # Lower attack power
    
    # Evil Wizard's Regen Health Attack Up
    def regenerate(self):
        if not self.poison:
            self.health += 5  # Lower regeneration amount
            self.attack_power += 2
            print(f"{self.name} regenerates 5 health! \nCurrent health: {self.health}, attack power: {self.attack_power}\n")