import random

my_dict = {
    '4267': "wolfpack",
    '7342': "rapiers",
    '197': "oorials",
    '173': "panthers",
    '854': "the tigers",
    '1298': "thunderbirds",
    '1862': "bulls",
    '7': "hawks",
    '189': "daggers",
    '27864': "flying bullets",
    '65120': "eight pursoots",
    '31': "scorpions",
    '412': "lions",
    '9999': "lightnings",
    '9867': "rhinos",
    '123': "cobras",
    '340': "black cobras",
    '366': "battle axes",
    '385': "black archers",
    '4': "flying daggers",
}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())


def get_query(x):
    s = "You have " + str(
        x) + "seeds with you to feed chicken and if the chicken is happy it will provide you with the answer to this " \
             "level. "
    return s


def getseed():
    x = random.sample(key_list, 1)[0]
    return x, my_dict[x]
