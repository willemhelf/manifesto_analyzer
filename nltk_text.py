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
from pathlib import Path

###

def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r') as f:
        data = f.read()
        printout_test(data)


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
    stop_words = set(stopwords.words("english"))
    for word in text:
      if word not in stop_words:
        stripped_set.add(word)
    return stripped_set


'''find the top ten words used in the text'''

def top_ten(words):
   frequency_distribution = FreqDist(words)
   return frequency_distribution.most_common(10)


'''print out top ten words to the console'''

def print_top_ten(text):
   prepared = prepare_text(text)
   no_stopwords = remove_stopwords(prepared)
   top_ten_words = top_ten(no_stopwords)
   print(top_ten_words)


'''run file'''

directory = Path('texts')

for file in directory.glob('*.txt'):
    process_file(file)