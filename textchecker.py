import os
from nltk.tokenize import RegexpTokenizer
import hunspell
import pandas as pd

hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
tokenizer = RegexpTokenizer(r'\w+')


def check_length(text):
    '''finds the length of each text, and returns if it is in the range

    :param text: the text
    :return: number of words, bool of if the words are in the range
    '''
    words = tokenizer.tokenize(text)
    length = len(words)
    bool_length = (length < 360) and (length > 300)
    return length, bool_length


def check_spelling(text):
    '''finds how many spelling errors are in each text

    :param text: the text
    :return: number of errors
    '''
    num_incorrect = 0
    words = tokenizer.tokenize(text)
    for element in words:
        if not hobj.spell(element):
            num_incorrect += 1
    return num_incorrect


def sort_files(list):
    '''sorts the list because for some reason its in random order
    :param list: list
    :return: sorted list
    '''
    list.sort(key=lambda x: int(x.split('_')[0]))
    return list

def make_dictionary_list(path, columns):
    '''this goes through folder and creates the list of dictionaries

    :param soup: beautiful soup object
    :param columns: list of the colums for the data
    :param types: list of types for the data
    :return: returns the list of dictionaries
    '''
    dictionaries = []
    files = sort_files(os.listdir(path))
    for filename in files:
        file = open(path+'/'+filename, 'r')
        text= file.read()
        text_info = {}
        text_info[columns[0]] = filename
        length, bool_length = check_length(text)
        text_info[columns[1]] = length
        text_info[columns[2]] = bool_length
        incorrect = check_spelling(text)
        text_info[columns[3]] = incorrect
        dictionaries.append(text_info)
        print(text_info)
    return dictionaries


def main(path):
    ''' looks through the files of a directory, and creates a table with
        the number of words, mispelled words in each text

    :param path: the directory
    '''
    columns = ['filename', 'length', 'in range?', 'number of incorrect words']
    output = make_dictionary_list(path, columns)
    table = pd.DataFrame.from_records(output, columns=columns)
    print(table)
    table.to_csv(path_or_buf='experiences_table.csv')


main('/home/downey/PycharmProjects/questions/Experiences in life')