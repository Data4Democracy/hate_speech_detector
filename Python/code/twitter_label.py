
import pandas
import numpy as np
import re

tweets = pandas.read_csv('~/Documents/final_tweets_NLP+CSS_2016.csv', header = None)
tweets['label'] = 0

badwords = pandas.read_csv('~/Documents/list1.csv', header = None)

for i in range(0, len(badwords)):
    
    print(badwords[0][i])
    tweets["label"] = tweets["label"] + [1 if badwords[0][i] in ele else 0 for ele in tweets[1]]




badwords = pandas.read_csv('~/Documents/list2.csv', header = None)

for i in range(0, len(badwords)):
    text = re.findall('\"(.*?)\"', badwords.loc[i][0])
    print(text)
    tweets["label"] = tweets["label"] + [1 if text[0] in ele else 0 for ele in tweets[1]]
    

badwords = pandas.read_csv('~/Documents/list3.csv', header = None)

for i in range(0, len(badwords)):
    
    print(badwords[0][i])
    tweets["label"] = tweets["label"] + [1 if badwords[0][i] in ele else 0 for ele in tweets[1]]



badwords = pandas.read_csv('~/Documents/list4.csv', header = None)

for i in range(0, len(badwords)):
    
    print(badwords[0][i])
    tweets["label"] = tweets["label"] + [1 if badwords[0][i] in ele else 0 for ele in tweets[1]]


badwords = pandas.read_csv('~/Documents/list5.csv', header = None)

for i in range(0, len(badwords)):
    text = badwords.loc[i][0].split(',')
    print(text)
    tweets["label"] = tweets["label"] + [1 if text[0] in ele else 0 for ele in tweets[1]]


tweets['label'] = np.where(tweets['label']>=1, 1, 0)    


## sanity check
tweets['label'].sum()
