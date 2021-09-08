import pandas as pd 
import numpy as np 
import nltk
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm')
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from word_files import stop_words_lst

class DataPreproc:
    '''Here we will be removing the stopwords and punctuation marks from the given text data'''

#-----------------------------------*****************------------------------------------------------#
    '''Below function removes the punctuation marks from the text data : Arg -- (original text data)'''
    @staticmethod
    def puncRemove(text_data):
        data_nopunc = text_data.translate(str.maketrans('','', string.punctuation))
        return(data_nopunc)

    ''' Below function removes all the stopwords from the new no punctuation data : 
        Arg -- (new data from previous function) '''
    @staticmethod
    def stopwRemove(nopunc_data):
        token_word = word_tokenize(nopunc_data)
        filtered_data = ' '.join([word for word in token_word if nlp.vocab[word].is_stop == False and word not in stop_words_lst])       
        return(filtered_data)
    
    '''Below function checks for non-english words as well as unwanted characters and thus removes
       them : Arg -- (filtered data with no stopwords and no punctuations) '''
    @staticmethod
    def nonEnglish(filter_data):
        return(' '.join([w for w in filter_data.split() if w in re.sub(r"[^A-Za-z]", " ", w.strip())]))
                