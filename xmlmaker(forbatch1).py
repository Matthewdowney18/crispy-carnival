import re
from bs4 import BeautifulSoup

# open the file
batch = open('batch 1 (cleaned) (added questions)', 'r')

# using beautiful soup
soup = BeautifulSoup(features='xml')
soup.append(soup.new_tag("corpus", genre = "fiction"))

# counters
get_text = 0
q_number = 0
q_reader = 0
k = 0

def find_type(number):
    if number == '1':
        qu_type = 'Temporal_order'
    elif number == '2':
        qu_type = 'Coreference'
    elif number == '3':
        qu_type = 'Subsequent_state'
    elif number == '4':
        qu_type = 'Causality'
    elif number == '5':
        qu_type = 'Factual'
    elif number == '6':
        qu_type = 'Information_attribution'
    elif number == '7':
        qu_type = 'World_knowledge_misc'
    elif number == '8':
        qu_type = 'World_knowledge_duration'
    elif number == '9':
        qu_type = 'Unanswerable'
    else:
        qu_type = 'unknown'
    return qu_type


# goes through each line of the text
for line in batch:
    # finds the start of a new text, and creates the tag
    searchObj = re.search('Text:', line, re.M | re.I)
    if searchObj:
        text_id = line[6:10]    # name the texts
        text_tag = soup.new_tag("Text", id=text_id)
        soup.corpus.append(text_tag)

        body_tag = soup.new_tag("body") # create body tag
        text_tag.append(body_tag)
        get_text = 1  # activates the get text
        q_number = 0    # resets the question number
        continue

    searchObj = re.search('-----', line, re.M | re.I)
    if searchObj:
        get_text = 0
        continue

    # finds the text of the passage
    if get_text:
        body_tag.append(line)
        continue

    # finds each question and creates a tag
    searchObj = re.search('\[', line, re.M | re.I)
    if searchObj:
        q_type = find_type(line[1])
        q_tag = soup.new_tag("q", id=str(q_number), type=q_type, misspelled="", corrected="", replaced="")
        text_tag.append(q_tag)
        q_number += 1   # adds to the question number
        q_reader = 1    # activates the question reader
        k = 0           # resets the answer counter
        continue

    # searches for answers that always begin with a tab
    searchObj = re.search('\t', line, re.M | re.I)
    if searchObj:
        answer_tag = soup.new_tag("body")
        a_text = line[4:-1]  # find the text for the answers
        # assign the answers to their respective position with k
        answer_tag = soup.new_tag('a', id=k, correct="")
        q_tag.append(answer_tag)
        answer_tag.append(a_text) # addinf the text of the answer
        q_reader = 0 # deactivates the question reader
        k += 1
        continue

    # finds the text of the question
    if q_reader:
        q_tag.append(line)
        continue



# make the new file
print(soup.prettify())
f = open('batch1(spellchecked)', 'w')
f.write(str(soup.prettify()))








