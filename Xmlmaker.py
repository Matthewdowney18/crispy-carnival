import re
from bs4 import BeautifulSoup

# open the file
batch = open('batch3(spellchecked).txt', 'r')

# using beautiful soup
soup = BeautifulSoup(features='xml')
soup.append(soup.new_tag("corpus", genre = "fiction"))

# counters
get_text = 0
q_number = 1
q_reader = 0
k = 0

# goes through each line of the text
for line in batch:
    # finds the start of a new text, and creates the tag
    searchObj = re.search('Text', line, re.M | re.I)
    if searchObj:
        text_id = 'f' + line[11:14]    # name the texts
        text_tag = soup.new_tag("Text", id=text_id)
        soup.corpus.append(text_tag)
        q_number = 1    # resets the question number
        continue

    # finds each question and creates a tag
    search = 'Q' + str(q_number) + ' '
    searchObj = re.search(search, line, re.M | re.I)
    if searchObj:
        q_type = line[4: -2]
        q_tag = soup.new_tag("q", id=str(q_number), type = q_type , misspelled="", corrected="", replaced="")
        text_tag.append(q_tag)
        q_number += 1   # adds to the question number
        get_text = 0    # deactivates the get text
        q_reader = 1    # activates the question reader
        k = 0           # resets the answer counter
        continue

    # searches for answers that always begin with a tab
    searchObj = re.search('\t', line, re.M | re.I)
    if searchObj:
        answer_tag = soup.new_tag("body")
        a_text = line[4:-1]  # find the text for the answers
        # assign the answers to their respective position with k
        if k == 0:   # making tags for the respective answers
            answer_tag = soup.new_tag('A', correct="")
        elif k == 1:
            answer_tag = soup.new_tag("B", correct="")
        else:
            answer_tag = soup.new_tag("C", correct="")
        q_tag.append(answer_tag)
        answer_tag.append(a_text) # addinf the text of the answer
        q_reader = 0 # deactivates the question reader
        k += 1
        continue

    # finds the text of the question
    if q_reader:
        q_tag.append(line)
        continue

    # finds the text of the passage
    if get_text:
        body_tag.append(line)
        continue

    # creats the body tag
    searchObj = re.search('WorkerId', line, re.M | re.I)
    if searchObj:
        body_tag = soup.new_tag("body")
        text_tag.append(body_tag)
        get_text = 1 # activates the get text
        continue

# make the new file
print(soup.prettify())
f = open('batch3(spellchecked)', 'w')
f.write(str(soup.prettify()))