import random
import time

def pick_a_pair():
    names = ["Leke","Moses","Divine","Esther","Taiwo A","Kenny","Dozie","Stonecold",
             "Olash","Stephen","AZ","Mario","Edwin","Christopher","Uzo","Taiwo",
             "Daniel","Christian","Onyinye","AY","Samuel","Hamid","Tosin","Malik",
             "Bibi","Ifeanyi","James","Olumide","Mercy","Gloria","Favour","Christianah"]

    random.shuffle(names)

    print("In the left corner we have...")
    time.sleep(2)
    print(names[0].upper() + "!!!")
    print("And in the right corner we have...")
    time.sleep(2)
    print(names[1].upper() + "!!!")
    time.sleep(1)
    print("Let The Code War Commence!")

    return [names[0], names[1]]

pick_a_pair()