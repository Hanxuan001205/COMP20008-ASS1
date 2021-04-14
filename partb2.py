import os
import re
import string
def get_words(txt):
    words = []
    for line in txt.readlines():
        line = line.strip('\n')
        line = line.strip(string.digits)
        line = line.strip(string.punctuation)
        line= line.rstrip(string.punctuation)
        for word in line.split():
            words.append(word)
    txt.close()
    return words
def  llegal_text(words):
    text = ''
    for i in words:
        i = i.lower()
        i = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', i, re.S)
        i = "".join(i)
        text = text + i + ' '
    return text
root_book = []
d = {}
for r,dirs,files in os.walk('cricket'):
    for file in files:
        f = os.path.join(r,file)
        root_book.append(f)
for root in root_book:
    basename = os.path.basename(root)
    txt = open(root)
    new = llegal_text(get_words(txt))
    d[basename] = new
keys = []
for i in d.keys():
    keys.append(i)
for i in range(len(root_book)-1):
    new = d[keys[i]]
