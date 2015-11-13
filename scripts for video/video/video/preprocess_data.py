import re
import string
import nltk

from nltk.corpus import stopwords
stop = stopwords.words('english')


pattern = "(20[01][0-9])\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])\s[012][0-9]\:[0-5][0-9]\:[0-5][0-9]                .*$"
pattern1= "^[0-9]*    [0-9]*?"
fin = open("tweets_output/5444512.txt","r")
fout = open("tweets_output/5444512_clean.txt","a")

print "Preprocessing the tweet corpus"
for line in fin:
    if line.strip():
        result = re.sub(r"http\S+", "", line)
        result = re.sub(r"^RT", "", line)
        valid_characters = string.ascii_letters + string.digits + " " + "@" + "#"
        result = ''.join([c for c in result if c in valid_characters])   
        final =[i for i in result.split() if i not in stop]
        joined_string = ' '.join(final)
        fout.write(str(joined_string))
        fout.write('\n')

print "Stopword removal complete"
