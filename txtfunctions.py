import sys
import os
import time
from game import stats


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

def txt_item_shop_book(itemname, cost):
    print((' Name: {}: {}').format(itemname, cost))

def print_stats():
    for item in stats:
        print(('Name: {}').format(item["name"]))
        print(('Hp\Maxhp: {}/{}').format(item["hp"], item["maxhp"]))
        print(('Dmg: {}').format(item["dmg"]))
        print(('Helth potions: {}').format(item["potion"]))
        print(('Gold: {}').format(item["gold"]))
        print(('Bag: {}').format(item["bag"]))
        print(('Diamonds: {}').format(item["diamonds"]))