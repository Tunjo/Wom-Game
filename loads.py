import json
from txtfunctions import clear_screen




def draw_txt(file):
    clear_screen()
    directory = open("draws\%s" % file, "r")
    draw = directory.read()
    print(draw)

def json_load():
    with open("txt.json") as file:
        global data1
        data1 = json.load(file)




def json_monster():
    with open("monsters\mnpc.json") as files:
        global npc1
        npc1 = json.load(files)



def json_load_shop():
    with open("shop\shop.json") as file:
        global shopitem1
        shopitem1 = json.load(file)




data = data1
npc = npc1
shopitem = shopitem1