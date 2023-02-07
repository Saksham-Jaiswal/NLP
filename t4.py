import nltk

from urllib import request
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

url = "https://www.gutenberg.org/cache/epub/69969/pg69969.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)
print(tokens[:20])

porter = PorterStemmer()
ans = porter.stem('fully')
print(ans) #fulli

porter = LancasterStemmer()
ans = porter.stem('happiness')
print(ans) #happy

porter = RegexpStemmer('ing')
ans = porter.stem('singing')
print(ans) #s

porter = SnowballStemmer('french')
ans = porter.stem('detester')
print(ans) #detest

porter = PorterStemmer()
li = tokens[:20]
for i in li:
    print(porter.stem(i))



