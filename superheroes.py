import random

class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

    def defend(self):
        total_defense = 0
        for add_defense in self.armors:
            total_defense += add_defense.defend()
        if self.health == 0:
            total_defense = 0
        return total_defense

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1
        
    def add_kill(self, num_kills):
        self.kills += num_kills

    #Not in tutorial
    def add_armor(self, armor):
        self.armors.append(armor)

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        self.lowest_attack = self.attack_strength // 2
        self.highest_attack = random.randint(self.lowest_attack, self.attack_strength)
        return self.highest_attack

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        for index in self.heroes:
           print(index.name)

    def attack(self, other_team):
        total_attack_power = 0
        for hero in self.heroes:
            total_attack_power += hero.attack()
        deaths = other_team.defend(total_attack_power)
        
        for hero in self.heroes:
            hero.add_kill(deaths)

#        It should call add_kill() on each hero with the number of kills made.

    def defend(self, damage_amt):
        total_defense_power = 0
        for hero in self.heroes:
            total_defense_power += hero.defend()
        total_excess = damage_amt - total_defense_power
        if total_excess > 0:
            return self.deal_damage(total_excess)
        else:
            return 0

    def deal_damage(self, damage):
        total_damage = damage // len(self.heroes)
        total_deaths = 0
        for hero in self.heroes:
            hero.take_damage(total_damage)
            #does not update total damage?
            if hero.health <= 0:
                total_deaths += 1
        return total_deaths

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = hero.start_health
    
    def stats(self):
        for hero in self.heroes:
            print(hero + "Kill/Death Ratio:")
            print(hero.deal_damage()/hero.take_damage())

    def update_kills(self):
        for hero in self.heroes:
            return True

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    def build_team_one(self):
        self.team_one = Team(input("What would you like Team One to be called?"))
        for hero in range(0,3):
            prompt_hero = input("What hero would you like to add to Team One?")
            print(prompt_hero + "has been added to Team One")
            self.team_one.add_hero(prompt_hero)
            prompt_ability = input("Alright what abilities should this hero have?")
            print(prom)

    def build_team_two(self):
        self.team_two = Team(input("What would you like Team Two to be called?"))
        for hero in range(0,3):
            prompt_hero = input("What hero would you like to add to Team Two?")
            print(prompt_hero + "has been added to Team Two")
            self.team_two.add_hero(prompt_hero)

    def team_battle(self):
        
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        for hero in self.team_one:
            hero.stats()
        for hero in self.team_two:
            hero.stats()
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """        

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack()) 
    ability = Ability("Divine Speed", 300) 
    hero.add_ability(ability) 
    print(hero.attack()) 
    new_ability = Ability("Super Human Strength", 800) 
    hero.add_ability(new_ability) 
    print(hero.attack())

# team = Team("yo")
# jodie = Hero("Jodie Foster")
# batman = Hero("Batman")
# ww = Hero("Wonder Woman")

# team.add_hero(jodie)
# team.add_hero(batman)
# team.add_hero(ww)
# print(len(team.heroes))

# team.remove_hero(jodie)

# print(len(team.heroes))

