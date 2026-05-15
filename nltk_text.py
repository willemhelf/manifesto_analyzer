###imports
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import FreqDist
nltk.download('punkt_tab')
nltk.download('stopwords')
import string

###

file = 'dada.txt'
file_text = open(file).read()

'''To prepare text for analysis, we remove punctuation and 
put all words in lowercase. We then break it down into a set
of individual words.
'''

def prepare_text(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    quote_marks = {ord('\u2018'): None, ord('\u2019'): None}
    cleaned = clean_text.translate(quote_marks)
    return word_tokenize(cleaned.lower())


'''Remove stopwords from text for better content analysis'''

def remove_stopwords(text):
    stripped_set = set()
    stop_words = set(stopwords.text("english"))
    for word in text:
      if word not in stop_words:
        stripped_set.add(word)
    return stripped_set

'''main function – return us the ten most common words'''

if __name__ == '__main__':
    prepared_text = prepare_text(file_text)
    stripped_set = set()
    stop_words = set(stopwords.words("english"))
    for word in prepared_text:
      if word not in stop_words:
        stripped_set.add(word)
    distribution = FreqDist(stripped_set)
    print(distribution)