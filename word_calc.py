import re
from word_files import pos_words_dict
from word_files import neg_words_dict

'''Here we will be calculating the number of positive and negative words, percentage of contribution and
also the list of words itself.'''
'''Input Arguments : Cleaned data '''
'''Output : Percentage of Positive words, positive words, Percentage of negative words, negative'''

def wordToken(cleaned_data):
    new_tokenize_words = re.findall(r'\b\w[\w-]*\b', cleaned_data.lower())
    return(new_tokenize_words)

def pos_wordMine(new_token_data):
    num_pos_words = 0
    num_words = len(new_token_data)
    pos_words = []
    for word in new_token_data:
        if word in pos_words_dict['pos']:
            pos_words.append(word)
            num_pos_words = num_pos_words +  1
        
        percent_pos = (num_pos_words / num_words)

    return(percent_pos,set(pos_words))

def neg_wordMine(new_token_data):
    num_neg_words = 0
    num_words = len(new_token_data)
    neg_words = []
    for word in new_token_data:
        if word in neg_words_dict['neg']:
            neg_words.append(word)
            num_neg_words = num_neg_words +  1
        
        percent_neg = (num_neg_words / num_words)

    return(percent_neg,set(neg_words))

