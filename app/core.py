import pandas as pd
import numpy as np
from sklearn.externals import joblib
from app.config import TRAINING_DATA_LOCATION, MODEL_LOCATION


class GlobalDataLoad(type):
    """ Metaclass used to load data before app begins."""
    def  __new__(meta, name, bases, clzdict):
        cls = super().__new__(type,name,bases,clzdict)

        df = pd.read_csv(TRAINING_DATA_LOCATION, encoding='latin-1')
  
        cls.X=df['tweet']
        cls.y=df['class']

        return cls


class DataStore(metaclass=GlobalDataLoad):    


    @classmethod
    def get_random_test(cls):
        ind = np.random.choice(len(cls.X))
        return cls.X.iloc[ind], cls.y.iloc[ind]


class GlobalModelLoad(type):
    """ Metaclass used to load and train the model before app begins."""
    def  __new__(meta, name, bases, clzdict):
        cls = super().__new__(type,name,bases,clzdict)

        # Load model
        cls._model = joblib.load(MODEL_LOCATION)

        return cls


class Model(metaclass=GlobalModelLoad):
        
    @classmethod
    def predict(cls, X):
        """ X should be a list of strings."""
        return [{ "text" : k, "label" : int(v)} for k,v in zip(X,cls._model.predict(X))] # cast to int for json, remove numpy type


