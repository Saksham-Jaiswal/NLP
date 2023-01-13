import nltk

from nltk.book import *

from nltk.corpus import brown

a = brown.categories()
print(a)

hr = brown.words(categories='humor')
print(hr)

