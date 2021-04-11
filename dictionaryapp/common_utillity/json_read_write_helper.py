import json
import os
from ..models import Dictionary

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'data\\data\\DA.json')


def read_json_data():
    # Opening JSON file
    f = open(file_path, )

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    inc_variable = 0
    for word in data:
        # print("====>", word, "==========>", data[word]['ANTONYMS'], data[word]['SYNONYMS'])
        meaning = ""
        if data[word]['MEANINGS']:
            meaning = data[word]['MEANINGS']

    # Closing file
    f.close()
    return data


def filter_json_data(words_json_data):
    break_variable = 0
    # print("----->", words_json_data)

    for word in words_json_data:
        # print("====>", word, "==========>", words_json_data[word]['ANTONYMS'], words_json_data[word]['SYNONYMS'])
        if break_variable == 100:
            break
        break_variable += 1

        # formats synonyms here
        synonyms = ""
        if words_json_data[word]['SYNONYMS']:
            for synonym in words_json_data[word]['SYNONYMS']:
                synonyms += synonym + ", "

        # formats antonyms here
        antonyms = ""
        if words_json_data[word]['ANTONYMS']:
            for antonym in words_json_data[word]['ANTONYMS']:
                antonyms += antonym + ", "

        # formats meaning here
        meanings = ""
        if words_json_data[word]['MEANINGS']:
            keys = list(words_json_data[word]['MEANINGS'].keys())
            for key in keys:
                flag = 0
                for meaning in words_json_data[word]['MEANINGS'][key]:
                    if flag == 2:
                        break
                    meanings += meaning + ", "
                    flag += 1
                break
        print("-----------------=>meaning", meanings)
        print("-----------------=>", synonyms)
        print("-----------------=>", antonyms)
        print("-----------------=>", word)
        dictionary_object = Dictionary(word=word, meaning=meanings, antonyms=antonyms, synonyms=synonyms, usage="")
        dictionary_object.save()
