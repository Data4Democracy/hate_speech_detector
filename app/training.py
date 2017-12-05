import nltk

# download necessary components
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
import nltk

from app.config import TRAINING_DATA_LOCATION, MODEL_LOCATION
from app.data_science import SentimentVectorizer, preprocess, tokenize, PosTfidfVectorizer, stopwords


# Train Model and Save

vectorizer = TfidfVectorizer(
    tokenizer=tokenize,
    preprocessor=preprocess,
    ngram_range=(1, 3),
    stop_words=stopwords,
    use_idf=True,
    smooth_idf=False,
    norm=None,
    decode_error='replace',
    max_features=10000,
    min_df=5,
    max_df=0.75
    )
pos_vectorizer = PosTfidfVectorizer()
sentiment_vectorizer = SentimentVectorizer()

model = Pipeline( [('features', FeatureUnion([('tfidf', vectorizer),('pos_tfidf', pos_vectorizer), 
                                             ('sentiment',sentiment_vectorizer)])),
                  ('feature_selector', SelectFromModel(LogisticRegression(class_weight='balanced',penalty="l1",C=0.01))),
                  ('model', LogisticRegression(class_weight='balanced',penalty='l2',C=0.01))] )

df = pd.read_csv(TRAINING_DATA_LOCATION, encoding='latin-1')

X = df['tweet']
y = df['class']

model.fit(X,y)
joblib.dump(model, MODEL_LOCATION)
