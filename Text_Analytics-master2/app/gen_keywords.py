from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train', shuffle = True)
newsgroups_test = fetch_20newsgroups(subset='test', shuffle = True)
newsgroups_train.data[:2]
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(400)
import nltk
nltk.download('wordnet')
import pandas as pd

stemmer = SnowballStemmer("english")

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

#Tokenize and lemmatize
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
             result.append(lemmatize_stemming(token))
    return result

def get_keywords(essay):
    document_num = 50
    doc_sample = essay
    words = []
    for word in doc_sample.split(' '):
        words.append(word)
    abc=preprocess(doc_sample)
    return abc