import re
import json

# open the file
batch = open('batch 1 (cleaned) (added questions)', 'r')

text = {}
m = 0
n = 0
t_text = ''
name = ''

for line in batch:
    searchObj = re.search('-', line, re.M | re.I)
    if searchObj and n == 1:
        n = 0
        text[name]['text']= t_text
        continue

    if n == 1:
        t_text += line[0:-1]
        continue

    # create the dictionary for each text
    searchObj = re.search('Text:', line, re.M | re.I)
    if searchObj:
        name = 'text ' + line[6:10]  # name the texts
        text[name] = {'text' : '', 'questions' : {}}
        j = 0   # reset the counter for the questions
        n = 1
        continue

    if m == 1:
        q_text = line[0:-1]  # find the text of the question
        text[name]['questions'][question] = {'type': q_type, 'text': q_text, 'answers': {'A': '', 'B': '', 'C': ''}}
        m = 0
        continue

    # create a dictionary for each question
    searchObj = re.search('\[', line, re.M | re.I)
    if searchObj:
        question = 'Q ' + str(j)
        q_type = line[1]        # find the type of the question
        j += 1                  # add to the counter for the question
        k = 0                   # reset the counter for the answers
        m = 1                   # activate the question reader
        continue

    searchObj = re.search('\t', line, re.M | re.I)
    if searchObj:
        a_text = line[4:-1] # find the text for the answers
        # assign the answers to their respective position with k
        if k == 0:
            text[name]['questions'][question]['answers']['A'] = a_text
        elif k == 1:
            text[name]['questions'][question]['answers']['B'] = a_text
        else:
            text[name]['questions'][question]['answers']['C'] = a_text
        k += 1

print(text)
#with open("addedquestions.json", "w") as f:
   # json.dump(text, f)
