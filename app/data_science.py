import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedShuffleSplit

from app.config import TRAINING_DATA_LOCATION

class GlobalDataLoad(type):
    """ Metaclass used to load data before app begins."""
    def  __new__(meta, name, bases, clzdict):
        cls = super().__new__(type,name,bases,clzdict)

        df = pd.read_csv(TRAINING_DATA_LOCATION, encoding='latin-1')
  
        X=df['tweet']
        y=df['class']

        sss = StratifiedShuffleSplit(n_splits=1, test_size=.15, random_state=0)
        train_index, test_index = next(sss.split(X,y))

        cls.X_train = X.iloc[train_index]
        cls.X_test = X.iloc[test_index]
        cls.y_train = y.iloc[train_index]
        cls.y_test = y.iloc[test_index]

        return cls


class DataStore(metaclass=GlobalDataLoad):    

    @classmethod
    def get_training_data(cls):
        return cls.X_train, cls.y_train

    @classmethod
    def get_test_data(cls):
        return cls.X_test, cls.y_test

    @classmethod
    def get_random_test(cls):
        ind = np.random.choice(len(cls.X_test))
        return cls.X_test.iloc[ind], cls.y_test.iloc[ind]


class GlobalModelLoad(type):
    """ Metaclass used to load and train the model before app begins."""
    def  __new__(meta, name, bases, clzdict):
        cls = super().__new__(type,name,bases,clzdict)

        # Basic model. TODO: Clean up, add method for this.
        cls._model = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features = 2000, # wild guess
            stop_words = 'english',
            min_df=2, 
            ngram_range = (1,3))),
        ('et',ExtraTreesClassifier())
        ])


        # Train model. TODO: Add method
        X_train, y_train = DataStore.get_training_data()
        cls._model.fit(X_train,y_train)

        return cls



class Model(metaclass=GlobalModelLoad):
        
    @classmethod
    def predict(cls, X):
        """ X should be a list of strings."""
        return [{ "text" : k, "label" : int(v)} for k,v in zip(X,cls._model.predict(X))] # cast to int for json, remove numpy type


