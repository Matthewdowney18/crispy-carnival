import json
from nltk import word_tokenize
import hunspell
from bs4 import BeautifulSoup

hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')

with open('addedquestions.json') as f:
    texts = json.load(f)

soup = BeautifulSoup('', "lxml")
soup.append(soup.new_tag())
soup = BeautifulSoup(features='xml')

print(soup)

for item1 in texts:
    t_text = set(word_tokenize(texts[item1]['text']))
    for item2 in texts[item1]['questions']:
        q_text = set(word_tokenize(texts[item1]['questions'][item2]['text']))
        q_text -= {':'}
        matching = q_text & t_text      # finds the words from the question that match with the text
        not_found = q_text-matching     # finds the words from the question that do not match with the text
        for element in not_found:
            spell_bool = hobj.spell(element)
            #print(element, spell_bool)
        #print(q_text)

