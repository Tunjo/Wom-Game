import time
from txtfunctions import clear_screen, txt_flush
from loads import data, draw_txt, npc
from fight import fight_npc



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