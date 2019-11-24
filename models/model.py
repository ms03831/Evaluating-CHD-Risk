import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np 
from sklearn.metrics import accuracy_score

class Model:
    def __init__(self):
        self.model = None
        self.target = None
        self.features = None
        self.data = None
        self.testX = None
        self.testY = None
        self.trainX = None
        self.trainY = None
        
    def _readDataset(self, filename):
        self.data = pd.read_csv(filename)

    def _dropNulls(self):
        self.data.drop(["education"], axis = 1, inplace = True) #dropping this improved accuracy
        self.data.dropna(inplace = True)
    
    def _saveProcessedData(self):
        self.features = self.data.drop("TenYearCHD", axis = 1)
        self.target = self.data.TenYearCHD
        self.data.to_csv("../data/processedData.csv")
    
    def _trainTestSplit(self):
        self.trainX, self.testX, self.trainY, self.testY = train_test_split(self.features, self.target, test_size=0.2)
    
    def preProcessing(self, filename):
        self._readDataset(filename)
        self._dropNulls()
        self.data.reset_index(drop = True)
        self._saveProcessedData()
        self._trainTestSplit()
        #display(self.data.corr())
    
    def fit_model(self):
        lm = LogisticRegression(solver = 'lbfgs', max_iter = 100)
        print(np.array(self.trainX).shape)

        lm.fit(np.array(self.trainX), np.array(self.trainY))
        predictions = lm.predict(self.testX)
        print(accuracy_score(predictions, self.testY))
        
for i in range(10):        
    model = Model()
    model.preProcessing("../data/framingham.csv")
    model.fit_model()