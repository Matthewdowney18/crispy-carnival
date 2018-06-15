import re
import json

# open the file
batch = open('batch 1 (cleaned)', 'r')

text = {}
i = 0

for line in batch:
    # create the dictionary for each text
    searchObj = re.search('Text:', line, re.M | re.I)
    if searchObj:
        name = 'text ' + line[6:10]  # name the texts
        text[name] = {}
        i += 1  # add to the counter for texts
        j = 0   # reset the counter for the questions
        continue

    # create a dictionary for each question
    searchObj = re.search('\[', line, re.M | re.I)
    if searchObj:
        question = 'Q ' + str(j)
        q_text = line[3:-1]     # find the text of the question
        q_type = line[1]        # find the type of the question
        text[name][question] = {'text': q_text, 'type': q_type, 'question': {'A': '', 'B': '', 'C': ''}}
        j += 1                  # add to the counter for the question
        k = 0                   # reset the counter for the answers
        continue

    searchObj = re.search('\t', line, re.M | re.I)
    if searchObj:
        a_text = line[4:-1] # find the text for the answers
        # assign the answers to their respective position with k
        if k == 0:
            text[name][question]['question']['A'] = a_text
        elif k == 1:
            text[name][question]['question']['B'] = a_text
        else:
            text[name][question]['question']['B'] = a_text
        k += 1

with open("matt_questions.jason", "w") as f:
    json.dump(text, f)
