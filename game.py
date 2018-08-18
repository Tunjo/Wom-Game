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
        self.hp = 1000
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
        self.gold = 50
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

    def deal_dmg(self):
        dmgdone = random.randint(math.floor(self.dmg/2), self.dmg)
        txt_flush(data["dealdmg"] % dmgdone)
        return dmgdone



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
        print(('Helth potions: {}').format(item["potion"]))
        print(('Gold: {}').format(item["gold"]))
        print(('Bag: {}').format(item["bag"]))
        print(('Diamonds: {}').format(item["diamonds"]))


def print_inventory():
    for item in stats:
        print(('Chest: {}').format(item["inventory"]["chest"]))
        print(('Weapon: {}').format(item["inventory"]["weapon"]))
        print(('Offhand: {}').format(item["inventory"]["offhand"]))
        print(('Legs: {}').format(item["inventory"]["legs"]))
        print(('Magic: {}').format(item["inventory"]["magic"]))
        print(('Bag: {}').format(item["bag"]))


def json_load():
    with open("txt.json") as file:
        global data
        data = json.load(file)


def json_monster():
    with open("monsters\mnpc.json") as files:
        global npc
        npc = json.load(files)


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
    ask = input(" >> ")
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
    json_monster()
    txt_flush(data["option"])
    option = input(" >> ")
    if option == "1":
        explore_world()
    elif option == "2":
        inventory()
    else:
        pass

def inventory():
    clear_screen()
    print_stats()
    txt_flush(data["inventory"])
    options = input(" >> ")
    if options == "1":
        clear_screen()
        print_inventory()
        txt_flush_fast(data["inventory0"])
        equip = input(" >> ")
        for item in stats:

            if equip in item["bag"]:

                if equip == npc["winterslake"]["icepike"]["drops"][0]:
                    del_and_add_items_weapon(equip)
                    item["dmg"] += npc["winterslake"]["icepike"]["drop"]["sword"]
                    inventory()
                elif equip == npc["winterslake"]["icepike"]["drops"][1]:
                    del_and_add_items_weapon(equip)
                    item["dmg"] += npc["winterslake"]["icepike"]["drop"]["wand"]
                    inventory()
                elif equip == npc["winterslake"]["icepike"]["drops"][3]:
                    del_and_add_items_chest(equip)
                    item["hp"] += npc["winterslake"]["icepike"]["drop"]["chest"]
                    item["maxhp"] += npc["winterslake"]["icepike"]["drop"]["chest"]
                    inventory()

            else:
                clear_screen()
                print("Wrong entry!!!")
                time.sleep(2)
                inventory()
    elif options == "2":
        game_option()


def del_and_add_items_weapon(itemadd):
    for item in stats:
        if itemadd in item["bag"]:
            itemindex = item["bag"].index(itemadd)
            item["bag"].append(item["inventory"]["weapon"][0])
            item["inventory"]["weapon"].pop(0)
            item["inventory"]["weapon"].append(itemadd)
            item["bag"].pop(itemindex)

def del_and_add_items_chest(itemadd):
    for item in stats:
        if itemadd in item["bag"]:
            itemindex = item["bag"].index(itemadd)
            item["bag"].append(item["inventory"]["chest"][0])
            item["inventory"]["chest"].pop(0)
            item["inventory"]["chest"].append(itemadd)
            item["bag"].pop(itemindex)


def load_game():
    pass


def explore_world():
    clear_screen()
    draw_txt("world.txt")
    txt_flush(data["file"])
    inp = input(" >> ")
    if inp == "1":
        for item in stats:
            if npc["winterslake"]["icepike"]["gem"] in item["diamonds"]:
                print("Vec bio vamo!!")
                time.sleep(3)
                explore_world()
            else:
               ice_pike()
    elif inp == "6":
        game_option()
    else:
        sys.exit()

def npc_deal_dmg(npcdmg):
    dmg = random.randint(math.floor(npcdmg / 2), npcdmg)
    txt_flush(data["takedmg"] % dmg)
    return dmg

def fight_npc(jsonhp, txtnpcname, npcgem, npcdrops, npcquest, npcdmg):
    clear_screen()
    npchp = jsonhp

    print(data["option0"])
    option = input(" >>")
    if option == "1":
        while option == "1":
            clear_screen()
            print_stats()
            print(data["option1"])
            optioon = input(" >> ")
            if optioon == "1":
                if npchp <= 1:
                    clear_screen()
                    txt_flush(data["monsterdead"] % txtnpcname)
                    for item in stats:
                        item["diamonds"].append(npcgem)
                        drop = random.choice(npcdrops)
                        item["bag"].append(drop)
                        item["quest"].append(npcquest)
                        print_stats()
                        time.sleep(7)
                    game_option()
                else:
                    npchp -= Warrior.deal_dmg(Warrior)
                for item in stats:
                    if item["hp"] <= 1:
                        clear_screen()
                        txt_flush(data["dead"])
                        game_option()
                    else:
                        item["hp"] -= npc_deal_dmg(npcdmg)
            elif optioon == "2":
                pass
            elif optioon == "3":
                pass
            elif optioon == "4":
                pass
    elif option == "2":
        game_option()




def ice_pike():
    clear_screen()
    txt_flush(data["winter"])
    time.sleep(3)
    clear_screen()
    draw_txt("fish.txt")
    time.sleep(3)
    clear_screen()
    txt_flush(data["pike"])
    fight_npc(npc["winterslake"]["icepike"]["hp"], npc["winterslake"]["icepike"]["name"], npc["winterslake"]["icepike"]["gem"],
              npc["winterslake"]["icepike"]["drops"], npc["winterslake"]["icepike"]["quest"], npc["winterslake"]["icepike"]["dps"])













stats = []
players = []


intro_txt()
main_manu()


