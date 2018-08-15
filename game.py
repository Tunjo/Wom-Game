import sys
import os
import time
import random
import json
import math


class Player():
    def __init__(self, name):
        self.name = name

    def make_user(self):
        clear_screen()
        name = input("Name: ")
        self.name = name
        players.append(name)

class Warrior(Player):
    def __init__(self, hp, maxhp, dmg, inventory, potion, gold, bag):
        self.hp = hp
        self.maxhp= maxhp
        self.dmg = dmg
        self.inventory = inventory
        self.potion = potion
        self.gold = gold
        self.bag = bag


    def stats(self):
        self.hp = 1000
        self.maxhp = 100
        self.dmg = 50
        self.inventory = ["Rusty sword"]
        self.potion = 1
        self.gold = 50
        self.bag = []
        global player_stats
        player_stats = {
            "name": self.name,
            "hp": self.hp,
            "maxhp": self.maxhp,
            "dmg": self.dmg,
            "inventory": self.inventory,
            "potion": self.potion,
            "gold": self.gold,
            "bag": self.bag
        }

        stats.append(player_stats)

    def deal_dmg(self):
        dmgdone = random.randint(math.floor(self.dmg/2), self.dmg)
        txt_flush(data["dealdmg"] % dmgdone)
        return dmgdone






class Monsters():
    def __init__(self, name, hp, dmg, drops, gem, quest):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.drops = drops
        self.gem = gem
        self.quest = quest

    def take_dmg(self):
        dmg = random.randint(math.floor(self.dmg / 2), self.dmg)
        txt_flush(data["takedmg"] % dmg)
        return dmg



def draw_txt(file):
    clear_screen()
    directory = open("draws\%s" % file, "r")
    draw = directory.read()
    print(draw)


def print_stats():
    for item in stats:
        print(('Name: {}').format(item["name"]))
        print(('Hp\Maxhp: {}/{}').format(item["hp"], item["maxhp"]))
        print(('Dmg: {}').format(item["dmg"]))
        print(('Inventory: {}').format(item["inventory"]))
        print(('Helth potions: {}').format(item["potion"]))
        print(('Gold: {}').format(item["gold"]))
        print(('Bag: {}').format(item["bag"]))


def json_load():
    with open("txt.json") as file:
        global data
        data = json.load(file)



def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def txt_flush(txt):
    for i in txt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)


def txt_flush_fast(txt):
    for i in txt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


def intro_txt():
    clear_screen()
    json_load()
    txt_flush(data["intro"])
    time.sleep(2)


def main_manu():
    clear_screen()
    print("W.O.M.")
    print("1. START GAME")
    print("2. LOAD GAME")
    print("3. EXIT")
    ask = input("1, 2 or 3: ")
    if ask == "1":
        Player.make_user(Player)
        Warrior.stats(Warrior)
        game_option()
    elif ask == "2":
        load_game()
    else:
        sys.exit()


def game_option():
    clear_screen()
    json_load()
    txt_flush(data["option"])
    option = input("1, 2, 3, 4 or 5: ")
    if option == "1":
        explore_world()
    else:
        pass


def load_game():
    pass


def explore_world():
    clear_screen()
    draw_txt("world.txt")
    txt_flush(data["file"])
    inp = input("1, 2, 3, 4 or 5: ")
    if inp == "1":
        clear_screen()
        ice_pike()
    else:
        pass


def ice_pike():
    for item in stats:
        if "Ice Pike Diamond" == item["bag"]:
            sys.exit()
        else:
            clear_screen()
            txt_flush(data["winter"])
            time.sleep(3)
            clear_screen()
            draw_txt("fish.txt")
            time.sleep(3)
            clear_screen()
            txt_flush(data["pike"])
            print(data["option0"])
            option = input("1 or 2: ")
            if option == "1":
                Icepike = Monsters("Ice Pike Monster", 60, 30, ["Pike Sword", "Pike Scales", "Broken Wand", "Pike Rusty Dagger"], "Ice Pike Diamond", "Pike quest")
                while option == "1":
                    clear_screen()
                    print(data["option1"])
                    print_stats()
                    option = input(">> ")
                    if option == "1":
                        if Icepike.hp <= 1:
                            txt_flush(data["monsterdead"] % Icepike.name)
                            for item in stats:
                                Warrior.bag += Icepike.gem
                                drop = random.choice(Icepike.drops)
                                Warrior.bag += str(drop)
                                Warrior.bag += str(Icepike.quest)
                                print(Warrior.bag)
                                time.sleep(4)
                            game_option()
                        else:
                            Icepike.hp -= Warrior.deal_dmg(Warrior)

                        if item["hp"] <= 1:
                            txt_flush(data["dead"])
                            game_option()
                        else:
                           item["hp"] -= Icepike.take_dmg()
            elif option == "2":
                game_option()












stats = []
players = []


intro_txt()
main_manu()


