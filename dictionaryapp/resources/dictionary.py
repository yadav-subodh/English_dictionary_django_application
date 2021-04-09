from ..models import Dictionary


def add_new_word(word, meaning, synonyms, antonyms, usage):
    try:
        dictionary_object = Dictionary(word=word, meaning=meaning, antonyms=antonyms, synonyms=synonyms, usage=usage)
        dictionary_object.save()
        return {'message': "Word has added to dictionary, Thank You to increase number of words."}
    except Exception as exception:
        print(exception)
        return {'message': "something went wrong, please try again after sometime"}


def get_all_words():
    try:
        dictionary_object = Dictionary.objects.all()
        words_list = []
        for words in dictionary_object.iterator():
            word_dictionary = {'word': words.word, 'meaning': words.meaning, 'synonyms': words.synonyms,
                               'antonyms': words.antonyms, 'usage': words.usage}
            words_list.append(word_dictionary)
        return words_list
    except Exception as exception:
        print(exception)
        return [{'word': "", 'meaning': "", 'synonyms': "", 'antonyms': "", 'usage': ""}]


def get_words_by_matching(search_sting):
    try:
        dictionary_object = Dictionary.objects.filter(word__icontains=search_sting).filter(
            word__istartswith=search_sting)
        words_list = []
        for words in dictionary_object.iterator():
            word_dictionary = {'word': words.word, 'meaning': words.meaning, 'synonyms': words.synonyms,
                               'antonyms': words.antonyms, 'usage': words.usage}
            words_list.append(word_dictionary)
        print(words_list)
        return words_list
    except Exception as exception:
        print(exception)
        return [{'word': "", 'meaning': "", 'synonyms': "", 'antonyms': "", 'usage': ""}]
