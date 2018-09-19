from game import players, stats
from txtfunctions import clear_screen

class Player():
    def __init__(self, name):
        self.name = name

    def make_user(self):
        clear_screen()
        name = input("Name: ")
        self.name = name
        players.append(name)

class Warrior(Player):
    def __init__(self, hp, maxhp, dmg, inventory, potion, gold, bag, quest, diamonds):
        self.hp = hp
        self.maxhp= maxhp
        self.dmg = dmg
        self.inventory = inventory
        self.potion = potion
        self.gold = gold
        self.bag = bag
        self.quest = quest
        self.diamonds = diamonds


    def stats(self):
        self.hp = 100
        self.maxhp = 100
        self.dmg = 50
        self.inventory = {
            "chest": ["Ripped Chest"],
            "weapon": ["Rusty Sword"],
            "offhand": ["Book"],
            "legs": ["Ripped Legs"],
            "magic": []
        }
        self.potion = 1
        self.gold = 5000
        self.bag = []
        self.quest = []
        self.diamonds = []
        global player_stats
        player_stats = {
            "name": self.name,
            "hp": self.hp,
            "maxhp": self.maxhp,
            "dmg": self.dmg,
            "inventory": self.inventory,
            "potion": self.potion,
            "gold": self.gold,
            "bag": self.bag,
            "quest": self.quest,
            "diamonds": self.diamonds
        }

        stats.append(player_stats)