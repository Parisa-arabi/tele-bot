# bot_token = "6701853868:AAF2XERaXsNIlhyRTEmZU85bBqSDoedmAQ8"
# bot_user_name = "https://t.me/superdict_bot"
# URL = "the heroku app link that we will create later"
from PyMultiDictionary import MultiDictionary
from PyMultiDictionary import DICT_WORDNET


dictionary = MultiDictionary()


def get_mean(word):
    temp_mean = dictionary.meaning("en", word, dictionary=DICT_WORDNET)
    mean = ""
    for i in temp_mean.keys():
        mean = mean + str(i) + ":" + "\n"

        for j in temp_mean.values():
            mean = mean + ", ".join(j) + "\n"
    return mean


def get_syn(word):
    temp_syn = dictionary.synonym("en", word)
    syn = ""

    for j in temp_syn:
        syn = syn + j + "\n"
    return syn
# print(get_syn('jump'))

def count_word(word):
    pass
