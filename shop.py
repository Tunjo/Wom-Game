import time
from txtfunctions import clear_screen, print_stats, txt_flush, txt_item_shop_book
from loads import data, shopitem
from game import stats, game_option

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