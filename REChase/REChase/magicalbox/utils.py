import random

my_dict = {"Uno": 1, "Sita": 6, "Fin": 5, "Jeden": 1, "Tres": 3, "Pedwar": 4, "Hamza": 5,
           "Moja": 1, "Kolme": 3, "Sabbah": 7, "Tano": 5, "Wahed": 1, "Tessares": 4, "Odin": 1,
           "Fem": 5, "Satti": 7, "Ashta": 8, "Saba": 7, "Seis": 6, "Tissa": 9
           }

key_list = list(my_dict.keys())
val_list = list(my_dict.values())


def makeSequence():
    names = random.sample(key_list, 5)
    random.shuffle(names)
    result = 0
    for i in names:
        result = result * 10 + my_dict[i]

    temp = ', '.join(names[:4])
    temp = temp + " and " + names[4]
    return temp, result
