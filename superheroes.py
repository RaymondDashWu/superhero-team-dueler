import random

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for add_attack in self.abilities:
            total_attack += add_attack.attack()
        return total_attack

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

# FIXME: always have this method call at the bottom of the file
# to follow pep8 convention

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    # print(hero.attack()) 
    ability = Ability("Divine Speed", 300) 
    hero.add_ability(ability) 
    # print(hero.attack()) 
    new_ability = Ability("Super Human Strength", 800) 
    hero.add_ability(new_ability) 
    # print(hero.attack())

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
        #self.name = name
        # index = 0
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

team = Team("yo")
jodie = Hero("Jodie Foster")
batman = Hero("Batman")
ww = Hero("Wonder Woman")

team.add_hero(jodie)
team.add_hero(batman)
team.add_hero(ww)
print(len(team.heroes))

team.remove_hero(jodie)

print(len(team.heroes))

