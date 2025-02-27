import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, defense, accuracy, agility, stunned, poisoned, cooldown, special_abilities):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.max_health = health  # Store the original health for maximum limit
        self.accuracy = accuracy
        self.agility = agility
        self.stunned = stunned
        self.poison = poisoned
        self.special_abilities = special_abilities
        self.cooldown = cooldown
    
    def hit_chance(self):
        hit_chance = random.randint(1, 100) # Random number between 1 and 100
        return hit_chance
    
    def attack(self, opponent):

        chance = self.hit_chance() # Random number between 1 and 100
        if chance >= 90 or self.accuracy >= 100: # chance is 90+ or accuracy 100+ Critical Strike
            damage = random.randint(self.attack_power - 5, self.attack_power + 5)*2 #Randomized damage
            opponent.health -= damage-opponent.defense
            print(f"\n{self.name} attack was a Critical Strike! Damage - {damage}\n")
        elif chance <= self.accuracy - opponent.agility/2: #chance is less than accuracy then attack
            damage = random.randint(self.attack_power - 5, self.attack_power + 5) - opponent.defense
            if damage > 0:
                opponent.health -= damage
                print(f"\n{self.name} attacks {opponent.name} for {damage} damage!\n")
            else:
                print(f"{opponent.name} says, 'THAT TICKLES'")

                
        else: # if chance is greater than accuracy and under 90.
            print(f"\n{self.name} missed the attack!\n")
            
    def display_specials_list(self):
        print("")
        for keys in self.special_abilities:
            print(f"{keys}: {self.special_abilities[keys]}")
            
    def display_stats(self):
        print(f"{self.name}'s Stats - \nHealth: {self.health}/{self.max_health}, \nAttack Power: {self.attack_power}, \nAccuracy: {self.accuracy}")
    
   