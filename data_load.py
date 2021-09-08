import argparse
import pathlib
import json
import os
from data_prepocess import DataPreproc
from word_calc import pos_wordMine, neg_wordMine, wordToken
from sentiment_cal import sent_compute

class BaseClass:
    def __init__(self,**kwargs):
        if 'file' in kwargs:
            self.file = kwargs['file']

        data = DataPreproc.puncRemove(self.file)
        nopun_data = DataPreproc.stopwRemove(data)
        filtered_data = DataPreproc.nonEnglish(nopun_data)
        
        new_data = wordToken(filtered_data)
        self.positive_words_percent,self.positive_words = pos_wordMine(new_data)
        self.negative_words_percent,self.negative_words = neg_wordMine(new_data)


        self.subj_percent, self.pos_percent, self.neg_percent, self.neu_percent = sent_compute(filtered_data)
        

    def display_Sentscore(self):
        
        print(" Subjectivity Score (%) : {0:0.2f}".format(self.subj_percent),"\n",
              "Positive Polarity (%) : {0:0.2f}".format(self.pos_percent),"\n",
              "Negative Polarity (%) : {0:0.2f}".format(self.neg_percent),"\n",
              "Neutral Polarity (%) : {0:0.2f}".format(self.neu_percent))

    def display_Wordresult(self):

        print('Percentage of Positive Words : {:.0%}'.format(self.positive_words_percent))
        print("\n")
        print('All the Positive Words : {}'.format(self.positive_words))
        print("\n")
        print("__________________________****___________________________")
        print("\n")
        print('Percentage of Negative Words : {:.0%}'.format(self.negative_words_percent))
        print("\n")
        print('All the Negative Words : {}'.format(self.negative_words))



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-o" , "--option", help = "Enter the option score , words ")


    result = parser.parse_args()
    text_file_path = os.getcwd() + '\\' + 'text_data.txt'
    with open(text_file_path,'r') as read_file:
        data_file = json.load(read_file)

    data = data_file['body']

    obj = BaseClass(file = data)
    
    col_dict = {'score' : obj.display_Sentscore, 'words' : obj.display_Wordresult}

    for key in col_dict.keys():
        if result.option == key:
            col_dict[key]()


    

