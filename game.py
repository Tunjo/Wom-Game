import sys
import os
import time
import random
import json


class Player():
    def __init__(self, name):
        self.name = name

    def make_user(self):
        clear_screen()
        name = input("Name: ")
        self.name = name
        players.append(name)

class Warrior(Player):
    def __init__(self, hp, maxhp, dmg, inventory, potion):
        self.hp = hp
        self.maxhp= maxhp
        self.dmg = dmg
        self.inventory = inventory
        self.potion = potion


    def stats(self):
        self.hp = 100
        self.maxhp = 100
        self. dmg = 50
        self.inventory = ["Rusty sword"]
        self.potion = 1
        player_stats = {
            "name": self.name,
            "hp": self.hp,
            "maxhp": self.maxhp,
            "dmg": self.dmg,
            "inventory": self.inventory,
            "potion": self.potion
        }

        stats.append(player_stats)


class Monsters():
    def __init__(self, name, hp, maxhp, dmg, drop):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.dmg = dmg
        self.drop = drop


def map_desplay():
    clear_screen()
    mapfile = open("World.txt", "r")
    map = mapfile.read()
    txt_flush_fast(map)


def print_stats():
    for item in stats:
        print(('Name: {}').format(item["name"]))
        print(('Hp\Maxhp: {}/{}').format(item["hp"], item["maxhp"]))
        print(('Dmg: {}').format(item["dmg"]))
        print(('Inventory: {}').format(item["inventory"]))
        print(('Helth potions: {}').format(item["potion"]))


def json_load():
    with open("jsontxt.txt") as file:
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
    map_desplay()
    txt_flush(data["file"])
    inp = input("1, 2, 3, 4 or 5: ")
    if inp == "1":
        clear_screen()
        print("JEBOTE STO JE ZIMA")
    else:
        pass







stats = []
players = []


intro_txt()
main_manu()


