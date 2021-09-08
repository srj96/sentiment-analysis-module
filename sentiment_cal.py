from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

'''To calculate sentiment score of the given text data '''

def sentCal(new_data):
    sent_analyze = SentimentIntensityAnalyzer()
    pos_score = sent_analyze.polarity_scores(new_data)['pos']
    neg_score = sent_analyze.polarity_scores(new_data)['neg']
    neu_score = sent_analyze.polarity_scores(new_data)['neu'] 
    
    return(pos_score, neg_score, neu_score)

def get_adjectives(text):
    pos_tag_lst = ['JJ','JJR','JJS','RB','RBR','RBS']
    pos_text = nltk.pos_tag()
    
    return(' '.join([ word for (word,tag) in blob.tags if tag.startswith("JJ")]))

# def sent_compute(cleaned_data):
#     sent_analyze = SentimentIntensityAnalyzer()
#     pos_score = sent_analyze.polarity_scores(cleaned_data)['pos']
#     neg_score = sent_analyze.polarity_scores(cleaned_data)['neg']
#     neu_score = sent_analyze.polarity_scores(cleaned_data)['neu'] 

#     percent_score_pos = (pos_score)*100
#     percent_score_neg = (neg_score)*100
#     percent_score_neu = (neu_score)*100

#     blob  = TextBlob(cleaned_data)
#     subj = blob.sentiment.subjectivity *100

#     return(subj, percent_score_pos, percent_score_neg, percent_score_neu)




