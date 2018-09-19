import random
import time
import math
from game import stats, game_option
from txtfunctions import txt_flush_fast, txt_flush, clear_screen, print_stats
from loads import data


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