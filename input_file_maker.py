import pandas as pd
from bs4 import BeautifulSoup


# opening the files
with open('batch2(randomized)') as contents:
    soup = BeautifulSoup(contents, "xml")

with open('batch2(randomized)') as contents:
    soup.append(BeautifulSoup(contents, "xml").corpus)

# creating the colums header
columns = ['text', 'Q1', 'Q1_1', 'Q1_2', 'Q1_3', 'Q1_4','Q2',  'Q2_1', 'Q2_2', 'Q2_3', 'Q2_4', 'Q3', 'Q3_1', 'Q3_2',
           'Q3_3', 'Q3_4', 'Q4', 'Q4_1', 'Q4_2', 'Q4_3', 'Q4_4', 'Q5', 'Q5_1', 'Q5_2', 'Q5_3', 'Q5_4', 'Q6', 'Q6_1',
           'Q6_2', 'Q6_3', 'Q6_4', 'Q7', 'Q7_1','Q7_2', 'Q7_3', 'Q7_4', 'Q8', 'Q8_1', 'Q8_2', 'Q8_3', 'Q8_4', 'Q9',
           'Q9_1', 'Q9_2', 'Q9_3', 'Q9_4', 'Q10', 'Q10_1', 'Q10_2','Q10_3', 'Q10_4', 'Q11', 'Q11_1', 'Q11_2', 'Q11_3',
           'Q11_4', 'Q12', 'Q12_1', 'Q12_2', 'Q12_3', 'Q12_4', 'Q13', 'Q13_1', 'Q13_2','Q13_3', 'Q13_4', 'Q14', 'Q14_1',
           'Q14_2', 'Q14_3', 'Q14_4', 'Q15', 'Q15_1', 'Q15_2', 'Q15_3', 'Q15_4','Q16', 'Q16_1', 'Q16_2', 'Q16_3',
           'Q16_4', 'Q17', 'Q17_1', 'Q17_2', 'Q17_3', 'Q17_4', 'Q18', 'Q18_1', 'Q18_2', 'Q18_3', 'Q18_4']

types = ['Temporal_order', 'Coreference', 'Subsequent_state', 'Causality', 'Factual', 'Information_attribution',
         'World_knowledge_misc', 'World_knowledge_duration','Unanswerable']

text = soup.find_all('text')

def myfunction(arg1, arg2):
    '''

    :param arg1:
    :param arg2:
    :return:
    '''
    pass

dictionaries = []

for t in text:
    i = 0
    text_info = {}
    # adding the text
    text_info[columns[i]] = t.find('body').text.strip()
    i += 1
    for type in types:
        questions = t.find_all('q')
        for q in questions:
            j = 0
            if q["type"] == type and j < 2:
                j+=1
                # find the tags with the attributes and get the text
                # add the text of the question
                text_info[columns[i]] = q.text.splitlines()[1].strip()
                i+=1
                answers = q.find_all('a')
                # add the answers(already randomized
                for a in answers:
                    # need to clean text as well
                    text_info[columns[i]] = a.text.strip()
                    i += 1
    dictionaries.append(text_info)
    # the idea is that it builds the line for each text and then adds it to the table
    # i cant figure out how to make the list work at the moment however
table = pd.DataFrame.from_records(dictionaries, columns = columns)
print(table)
table.to_csv(path_or_buf='input_file.csv')

