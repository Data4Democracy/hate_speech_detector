import pandas as pd
import numpy as np
import nltk
from nltk.stem.porter import *
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *
from sklearn.base import BaseEstimator, TransformerMixin

stopwords=stopwords = nltk.corpus.stopwords.words("english")

other_exclusions = ["#ff", "ff", "rt"]
stopwords.extend(other_exclusions)

stemmer = PorterStemmer()

def preprocess(text_string):
    """
    Accepts a text string and replaces:
    1) urls with URLHERE
    2) lots of whitespace with one instance
    3) mentions with MENTIONHERE

    This allows us to get standardized counts of urls and mentions
    Without caring about specific people mentioned
    """
    space_pattern = '\s+'
    giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
        '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    mention_regex = '@[\w\-]+'
    parsed_text = re.sub(space_pattern, ' ', text_string)
    parsed_text = re.sub(giant_url_regex, '', parsed_text)
    parsed_text = re.sub(mention_regex, '', parsed_text)
    return parsed_text

def tokenize(tweet):
    """Removes punctuation & excess whitespace, sets to lowercase,
    and stems tweets. Returns a list of stemmed tokens."""
    tweet = " ".join(re.split("[^a-zA-Z]*", tweet.lower())).strip()
    tokens = [stemmer.stem(t) for t in tweet.split()]
    return tokens

def basic_tokenize(tweet):
    """Same as tokenize but without the stemming"""
    tweet = " ".join(re.split("[^a-zA-Z.,!?]*", tweet.lower())).strip()
    return tweet.split()

class PosTfidfVectorizer(BaseEstimator, TransformerMixin):
    """Get POS tags for tweets and transform via tfidf"""
    
    def __init__(self):
        self._pos_vectorizer = TfidfVectorizer(
            tokenizer=None,
            lowercase=False,
            preprocessor=None,
            ngram_range=(1, 3),
            stop_words=None,
            use_idf=False,
            smooth_idf=False,
            norm=None,
            decode_error='replace',
            max_features=5000,
            min_df=5,
            max_df=0.75,
            )    
    
    def _preprocess(self, X):
        tweet_tags = []
        for t in X:
            tokens = basic_tokenize(preprocess(t))
            tags = nltk.pos_tag(tokens)
            tag_list = [x[1] for x in tags]
            tag_str = " ".join(tag_list)
            tweet_tags.append(tag_str)
        return tweet_tags
    
    def fit(self, X, y=None):
        tweet_tags = self._preprocess(X)
        self._pos_vectorizer.fit(X)
        
        return self
    
    def transform(self, X, y=None):
        tweet_tags = self._preprocess(X)
        return self._pos_vectorizer.transform(X)

class SentimentVectorizer(BaseEstimator, TransformerMixin): 
    sentiment_analyzer = VS()

    def count_twitter_objs(self, text_string):
        """
        Accepts a text string and replaces:
        1) urls with URLHERE
        2) lots of whitespace with one instance
        3) mentions with MENTIONHERE
        4) hashtags with HASHTAGHERE

        This allows us to get standardized counts of urls and mentions
        Without caring about specific people mentioned.
        
        Returns counts of urls, mentions, and hashtags.
        """
        space_pattern = '\s+'
        giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
            '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        mention_regex = '@[\w\-]+'
        hashtag_regex = '#[\w\-]+'
        parsed_text = re.sub(space_pattern, ' ', text_string)
        parsed_text = re.sub(giant_url_regex, 'URLHERE', parsed_text)
        parsed_text = re.sub(mention_regex, 'MENTIONHERE', parsed_text)
        parsed_text = re.sub(hashtag_regex, 'HASHTAGHERE', parsed_text)
        return(parsed_text.count('URLHERE'),parsed_text.count('MENTIONHERE'),parsed_text.count('HASHTAGHERE'))

    def other_features(self, tweet):
        """This function takes a string and returns a list of features.
        These include Sentiment scores, Text and Readability scores,
        as well as Twitter specific features"""
        sentiment = self.sentiment_analyzer.polarity_scores(tweet)
        
        words = preprocess(tweet) #Get text only
        
        syllables = textstat.syllable_count(words)
        num_chars = sum(len(w) for w in words)
        num_chars_total = len(tweet)
        num_terms = len(tweet.split())
        num_words = len(words.split())
        avg_syl = round(float((syllables+0.001))/float(num_words+0.001),4)
        num_unique_terms = len(set(words.split()))
        
        ###Modified FK grade, where avg words per sentence is just num words/1
        FKRA = round(float(0.39 * float(num_words)/1.0) + float(11.8 * avg_syl) - 15.59,1)
        ##Modified FRE score, where sentence fixed to 1
        FRE = round(206.835 - 1.015*(float(num_words)/1.0) - (84.6*float(avg_syl)),2)
        
        twitter_objs = self.count_twitter_objs(tweet)
        retweet = 0
        if "rt" in words:
            retweet = 1
        features = [FKRA, FRE,syllables, avg_syl, num_chars, num_chars_total, num_terms, num_words,
                    num_unique_terms, sentiment['neg'], sentiment['pos'], sentiment['neu'], sentiment['compound'],
                    twitter_objs[2], twitter_objs[1],
                    twitter_objs[0], retweet]
        return features

    def get_feature_array(self, tweets):
        feats=[]
        for t in tweets:
            feats.append(self.other_features(t))
        return np.array(feats)

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return self.get_feature_array(X)