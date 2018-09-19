import time
from game import stats, game_option
from txtfunctions import clear_screen, print_stats, txt_flush, txt_flush_fast
from loads import data, npc


def print_inventory():
    for item in stats:
        print(('Chest: {}').format(item["inventory"]["chest"]))
        print(('Weapon: {}').format(item["inventory"]["weapon"]))
        print(('Offhand: {}').format(item["inventory"]["offhand"]))
        print(('Legs: {}').format(item["inventory"]["legs"]))
        print(('Magic: {}').format(item["inventory"]["magic"]))
        print(('Bag: {}').format(item["bag"]))

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