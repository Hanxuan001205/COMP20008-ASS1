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

def alter(file,old_str,new_str):
  with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
    for line in f1:
      if old_str in line:
        line = line.replace(old_str, new_str)
      f2.write(line)
  os.remove(file)
  os.rename("%s.bak" % file, file)

root_book = []
for r,dirs,files in os.walk('../pythonProject3/cricket'):
    for file in files:
        f = os.path.join(r,file)
        root_book.append(f)
for root in root_book:
    txt = open(root)
    llegal_text(get_words(txt))
