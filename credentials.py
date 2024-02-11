from PyMultiDictionary import MultiDictionary
from PyMultiDictionary import DICT_WORDNET
import logging

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
        mean= word + ' is not valid ' + 'choose meanining and enter again'
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
        syn = word + ' is not valid ' + 'choose synonym and enter again'
        return syn
        
# print(get_syn('jump'))

def count_word(word):
    pass
