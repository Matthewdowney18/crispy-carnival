import pandas as pd
from bs4 import BeautifulSoup
from random import shuffle


def get_columns(q_num, a_num):
    '''this function creates a list of column for the outut based on the nunber of questions and answers

    :param q_num: number of questions
    :param a_num: answers per question
    :return: list of columns
    '''
    c = ['text']
    for k in range(1, q_num +1):
        c.append('Q' + str(k)+' id')
        c.append(('Q' + str(k)))
        for l in range(1, a_num + 1):
            c.append('id')
            c.append(('Q'+str(k)+'_'+str(l)))
    return c


def get_rand_questions(questions, soup, types):
    list = []
    types = types+types
    for q in questions:
        answer_tag = soup.new_tag('a', id=3, correct="")
        q.append(answer_tag)
        answer_tag.append('unanswerable')  # addinf the text of the answer
        list.append(q)
    shuffle(list)
    shuffle(types)
    return list, types


def make_dictionary_list(soup, columns, types):
    '''this goes through the soup object and creates the list of dictionaries

    :param soup: beautiful soup object
    :param columns: list of the colums for the data
    :param types: list of types for the data
    :return: returns the list of dictionaried
    '''
    text = soup.find_all('Text')
    dictionaries = []
    for t in text:
        i = 0
        text_info = {}
        # adding the text
        text_info[columns[i]] = t.find('body').text.strip()
        i += 1
        questions = t.find_all('q')
        rand_questions, rand_types = get_rand_questions(questions, soup, types)

        for type in rand_types:
            for question in rand_questions:
                if question["type"] == type:
                    text_info[columns[i]] = question["id"]
                    i += 1
                    text_info[columns[i]] = question.text.splitlines()[1].strip()
                    i += 1
                    rand_questions.remove(question)
                    answers = question.find_all('a')
                    shuffle(answers)
                    for a in answers:
                        # the answer id does not work yet
                        text_info[columns[i]] = a["id"]
                        i += 1

                        text_info[columns[i]] = a.text.strip()
                        i += 1
                    break
        dictionaries.append(text_info)
    return dictionaries


def get_types(soup):
    '''this function finds the different type attributes and creates a list with them

    :param soup: the beautiful soup object with the data
    :return: the list of different types
    '''
    types = []
    questions = soup.find_all('q')
    for q in questions:
        if q["type"] not in types:
            types.append(q["type"])
    return types


def main():
    '''
    loads xml data files ang creates a dataframe that can be used to
    output questions and answers on a quiz
    '''
    # opening the files
    with open('batch2(spellchecked)(first added)') as contents:
        xml_data = BeautifulSoup(contents, "xml")

    with open('batch3(spellchecked)(first added)') as contents:
        xml_data.append(BeautifulSoup(contents, "xml").corpus)

    # creating the colums header
    columns = get_columns(18, 4)

    types = get_types(xml_data)

    output = make_dictionary_list(xml_data, columns, types)

    table = pd.DataFrame.from_records(output, columns = columns)
    print(table)
    table.to_csv(path_or_buf='input_file.csv')


main()