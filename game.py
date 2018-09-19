import json
import time
import sys
from txtfunctions import clear_screen, txt_flush, txt_flush_fast
from loads import json_load, json_monster, json_load_shop, draw_txt, data, npc
from classplayer import Player, Warrior
from inventory import inventory
from shop import shop
from monstersfight import witch_north, ice_pike


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

stats = []
players = []


intro_txt()
main_manu()


