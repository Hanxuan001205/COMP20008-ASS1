import os
import re
from main import get_words, llegal_text
return_root = []
key_words_set  = [input('keyword1: ')]
def b_search(keyword, txt):
    words = []
    for line in txt.readlines():
        for word in line.split():
            words.append(word)
    print(txt)
    """for i in words:
        if keyword == i:
            print(words)
            return True
    print(words)
    return False"""

root_book = []
for r,dirs,files in os.walk('/cricket'):
    for file in files:
        f = os.path.join(r,file)
        root_book.append(f)
if len(key_words_set)>5 or len(key_words_set)==0:
    print('The number of keywords cannot greater than 5 and greater than 0')
else:
    for i in key_words_set:
        keyword = i
        if len(return_root)==0:
            for root in root_book:
                txt = open(root)
                llegal_text(get_words(txt))
                if b_search(i, txt):
                    return_root.append(root)
        else:
            for root in return_root:
                txt = open(root)
                llegal_text(get_words(txt))
                if not b_search(i, txt):
                    return_root.remove(i)
for root in return_root:
    txt = open(root).read()
    first_line =  open(root).readline()
    if re.findall(r'[A-Z]{4}-\d{3}[A-Z]', txt):
        print(first_line)
        print(re.findall(r'[A-Z]{4}-\d{3}[A-Z]', txt))




