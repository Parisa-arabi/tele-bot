from PyMultiDictionary import MultiDictionary
from PyMultiDictionary import DICT_WORDNET
import logging
import json

dictionary = MultiDictionary()


def get_mean(word):
    try:
        logging.info(f"Getting meaning for word: {word}")
        temp_mean = dictionary.meaning("en", word, dictionary=DICT_WORDNET)
        mean = ""
        for i in temp_mean.keys():
            mean = mean + str(i) + ":" + "\n"
        for j in temp_mean.values():
            mean = mean + ", ".join(j) + "\n"
        return mean
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        mean = word + " is not valid " + "choose meanining and enter again"
        return mean


def get_syn(word):
    try:
        temp_syn = dictionary.synonym("en", word)
        syn = ""
        for j in temp_syn:
            syn = syn + j + "\n"
        return syn
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        syn = word + " is not valid " + "choose synonym and enter again"
        return syn


def user_data(message):
    with open("user_data.json", "r+") as f:
        chat_id = str(message.chat.id)
        data = json.load(f)
        if chat_id in data:
            if isinstance(data[chat_id]["word list"], str):
                data[chat_id]["word list"] = [data[chat_id]["word list"]]
            if message.text in data[chat_id]["word list"]:
                total = data[chat_id]["word list"].count(message.text)
                logging.info(f"count : {total+1}")

            data[chat_id]["word list"].append(message.text)
        else:
            data[str(message.chat.id)] = {"word list": message.text}
        f.seek(0)
        json.dump(data, f, indent=4)

def user_count(message):
    with open('user_data.json', 'r+') as f:
        chat_id = str(message.chat.id)
        
        