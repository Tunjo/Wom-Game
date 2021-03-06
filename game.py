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


def json_load_shop():
    with open("shop\shop.json") as file:
        global shopitem
        shopitem = json.load(file)


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
    print()
    print(" W.O.M.")
    print()
    print(" 1. START GAME")
    print(" 2. LOAD GAME")
    print(" 3. EXIT")
    print()
    ask = input(" >> ")
    if ask == "1":
        stats.clear()
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
    json_load_shop()
    txt_flush(data["option"])
    option = input(" >> ")
    if option == "1":
        explore_world()
    elif option == "2":
        inventory()
    elif option == "5":
        save_game()
    elif option == "6":
        shop()
    elif option == "7":
        main_manu()
    else:
        game_option()


def txt_item_shop_book(itemname, cost):
    print((' Name: {}: {}').format(itemname, cost))



def shop():
    clear_screen()
    print_stats()
    txt_flush(data["shop"])
    value = input(" >> ")
    if value == "1":
        clear_screen()
        print_stats()
        txt_flush(data["shop0"])
        ans = input(" >> ")
        if ans == "1":
            for item in stats:
                item["gold"] -= shopitem["potion"]
                item["potion"] += 1
            shop()
        elif ans == "2":
            shop()
    elif value == "2":
        clear_screen()
        print_stats()
        print()
        txt_item_shop_book(shopitem["books"]["book0"]["name"], shopitem["books"]["book0"]["cost"])
        txt_item_shop_book(shopitem["books"]["book1"]["name"], shopitem["books"]["book1"]["cost"])
        txt_item_shop_book(shopitem["books"]["book2"]["name"], shopitem["books"]["book2"]["cost"])
        txt_item_shop_book(shopitem["books"]["book3"]["name"], shopitem["books"]["book3"]["cost"])
        txt_item_shop_book(shopitem["books"]["book4"]["name"], shopitem["books"]["book4"]["cost"])
        txt_item_shop_book(shopitem["books"]["book5"]["name"], shopitem["books"]["book5"]["cost"])
        print()
        txt_flush(data["shop1"])
        itemname = input(" >> ")
        for item in stats:
            if itemname == shopitem["books"]["book0"]["name"] and item["gold"] >= shopitem["books"]["book0"]["cost"]:
                item["bag"].append(shopitem["books"]["book0"]["name"])
                item["gold"] -= shopitem["books"]["book0"]["cost"]
                shop()
            elif itemname == shopitem["books"]["book1"]["name"] and item["gold"] >= shopitem["books"]["book1"]["cost"]:
                item["bag"].append(shopitem["books"]["book1"]["name"])
                item["gold"] -= shopitem["books"]["book1"]["cost"]
                shop()
            elif itemname == shopitem["books"]["book2"]["name"] and item["gold"] >= shopitem["books"]["book2"]["cost"]:
                item["bag"].append(shopitem["books"]["book2"]["name"])
                item["gold"] -= shopitem["books"]["book2"]["cost"]
                shop()
            elif itemname == shopitem["books"]["book3"]["name"] and item["gold"] >= shopitem["books"]["book3"]["cost"]:
                item["bag"].append(shopitem["books"]["book3"]["name"])
                item["gold"] -= shopitem["books"]["book3"]["cost"]
                shop()
            elif itemname == shopitem["books"]["book4"]["name"] and item["gold"] >= shopitem["books"]["book4"]["cost"]:
                item["bag"].append(shopitem["books"]["book4"]["name"])
                item["gold"] -= shopitem["books"]["book4"]["cost"]
                shop()
            elif itemname == shopitem["books"]["book5"]["name"] and item["gold"] >= shopitem["books"]["book5"]["cost"]:
                item["bag"].append(shopitem["books"]["book0"]["name"])
                item["gold"] -= shopitem["books"]["book5"]["cost"]
                shop()
            else:
                clear_screen()
                txt_flush(data["shop3"])
                time.sleep(2)
                shop()
    elif value == "3":
        pass
    elif value == "4":
        pass
    elif value == "5":
        pass
    elif value == "6":
        pass
    elif value == "7":
        pass
    elif value == "8":
        game_option()
    else:
        clear_screen()
        txt_flush(data["invalid"])
        time.sleep(2)
        shop()


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
                elif equip == npc["winterslake"]["witch"]["drops"][0]:
                    del_and_add_items_weapon(equip)
                    item["dmg"] += npc["winterslake"]["witch"]["drop"]["wand"]
                    inventory()
                elif equip == npc["winterslake"]["witch"]["drops"][1]:
                    del_and_add_items_legs(equip)
                    item["hp"] += npc["winterslake"]["witch"]["drop"]["legs"]
                    item["maxhp"] += npc["winterslake"]["witch"]["drop"]["legs"]
                    inventory()
                elif equip == npc["winterslake"]["witch"]["drops"][2]:
                    del_and_add_items_chest(equip)
                    item["hp"] += npc["winterslake"]["witch"]["drop"]["robe"]
                    item["maxhp"] += npc["winterslake"]["witch"]["drop"]["robe"]
                    inventory()
                elif equip == npc["winterslake"]["witch"]["drops"][3]:
                    del_and_add_items_weapon(equip)
                    item["dmg"] += npc["winterslake"]["witch"]["drop"]["staff"]
                    inventory()
            else:
                clear_screen()
                print("Wrong entry!!!")
                time.sleep(2)
                inventory()
    elif options == "2":
        clear_screen()
        print_inventory()
        txt_flush_fast(data["invdelete"])
        opti = input(" >> ")

        if opti == "1":
            clear_screen()
            print_inventory()
            txt_flush_fast(data["invdelete0"])
            inp = input(" >> ")
            delete_item_bag_inventory(inp)
            inventory()

        elif opti == "2":
            inventory()

    elif options == "3":
        game_option()

    else:
        game_option()


def del_and_add_items_weapon(itemadd):
    for item in stats:
        if itemadd in item["bag"]:
            itemindex = item["bag"].index(itemadd)
            item["bag"].append(item["inventory"]["weapon"][0])
            item["inventory"]["weapon"].pop(0)
            default_dmg()
            item["inventory"]["weapon"].append(itemadd)
            item["bag"].pop(itemindex)


def del_and_add_items_chest(itemadd):
    for item in stats:
        if itemadd in item["bag"]:
            itemindex = item["bag"].index(itemadd)
            item["bag"].append(item["inventory"]["chest"][0])
            item["inventory"]["chest"].pop(0)
            default_hp()
            item["inventory"]["chest"].append(itemadd)
            item["bag"].pop(itemindex)


def del_and_add_items_legs(itemadd):
    for item in stats:
        itemindex = item["bag"].index(itemadd)
        item["bag"].append(item["inventory"]["legs"][0])
        item["inventory"]["legs"].pop(0)
        default_hp()
        item["inventory"]["legs"].append(itemadd)
        item["bag"].pop(itemindex)


def delete_item_bag_inventory(itemadd):
    for item in stats:
        if itemadd in item["bag"]:
            itemindx = item["bag"].index(itemadd)
            item["bag"].pop(itemindx)
        elif itemadd in item["inventory"]["weapon"]:
            item["inventory"]["weapon"].pop(0)
            default_dmg()
        elif itemadd in item["inventory"]["chest"]:
            item["inventory"]["chest"].pop(0)
            default_hp()
        elif itemadd in item["inventory"]["legs"]:
            item["inventory"]["legs"].pop(0)
            default_hp()
        elif itemadd in item["inventory"]["offhand"]:
            item["inventory"]["offhand"].pop(0)
            default_dmg()
        elif itemadd in item["inventory"]["magic"]:
            print("CANT DELETE MAGIC!!!")


def default_dmg():
    dmg = 50
    for item in stats:
        item["dmg"] = dmg


def default_hp():
    hp = 100
    for item in stats:
        item["hp"] = hp


def save_game():
    with open("savegame.json", "w+") as fp:
        fp.write(json.dumps(stats))
    game_option()


def load_game():
    with open("savegame.json", "r") as fp:
        file = json.load(fp)
    for item in file:
        clear_screen()
        txt_flush_fast(data["charload"])
        option = input(" >> ")
        if option == item["name"]:
            stats.clear()
            stats.append(item)
        else:
            clear_screen()
            txt_flush_fast(data["wrongname"])
            load_game()
    game_option()


def explore_world():
    clear_screen()
    draw_txt("world.txt")
    txt_flush(data["file"])
    inp = input(" >> ")
    if inp == "1":
        for item in stats:
            if npc["winterslake"]["icepike"]["gem"] in item["diamonds"]:
                if npc["winterslake"]["witch"]["gem"] in item["diamonds"]:
                    print("BIO VAMO")
                    explore_world()
                else:
                    witch_north()
            else:
               ice_pike()
    elif inp == "6":
        game_option()
    else:
        sys.exit()



def drink_potion():
    potion = random.randint(30, 100)
    for item in stats:
        if item["potion"] >= 1:
            item["potion"] -= 1
            item["hp"] += potion
            txt_flush_fast(data["potion0"] % potion)
            time.sleep(1)
        else:
            txt_flush_fast(data["potion"])
            time.sleep(1)
        if item["hp"] >= item["maxhp"]:
            item["hp"] = item["maxhp"]


def deal_dmg(dmg):
    dmgdone = random.randint(math.floor(dmg/2), dmg)
    txt_flush(data["dealdmg"] % dmgdone)
    return dmgdone


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
                    for item in stats:
                        npchp -= deal_dmg(item["dmg"])
                for item in stats:
                    if item["hp"] <= 1:
                        clear_screen()
                        item["hp"] = 0
                        txt_flush(data["dead"])
                        game_option()
                    else:
                        item["hp"] -= npc_deal_dmg(npcdmg)
            elif optioon == "2":
                pass
            elif optioon == "3":
                drink_potion()
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
    time.sleep(2)
    fight_npc(npc["winterslake"]["icepike"]["hp"], npc["winterslake"]["icepike"]["name"], npc["winterslake"]["icepike"]["gem"],
              npc["winterslake"]["icepike"]["drops"], npc["winterslake"]["icepike"]["quest"], npc["winterslake"]["icepike"]["dps"])


def witch_north():
    clear_screen()
    txt_flush(data["witch0"])
    time.sleep(3)
    clear_screen()
    draw_txt("witch.txt")
    time.sleep(3)
    clear_screen()
    txt_flush(data["witch1"])
    time.sleep(2)
    fight_npc(npc["winterslake"]["witch"]["hp"], npc["winterslake"]["witch"]["name"], npc["winterslake"]["witch"]["gem"],
              npc["winterslake"]["witch"]["drops"], npc["winterslake"]["witch"]["quest"], npc["winterslake"]["witch"]["dps"])




stats = []
players = []


intro_txt()
main_manu()


