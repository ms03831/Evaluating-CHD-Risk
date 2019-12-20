import numpy as np
from numpy import random

#sigmoid(z)
def sigmoid(z): 
    return 1/(1+np.exp(-z)) 

#MSE
def cost(yPred, y): 
    yPred, y = np.array(yPred), np.array(y)
    return 0.5*(yPred-y)**2

#derivative of cost 
def derivateCost(yPred, y): 
    return yPred - y

#iterator
def dataIter(batchSize, data):
    data = np.array(data)
    #random.shuffle(data)
    batches = []

    for i in range(0, np.array(data[0]).shape[0], batchSize):
        batchX, batchY = np.array(data[0][i:i+batchSize]), np.array(data[1][i:i+batchSize])
        batches.append([batchX, batchY])
    return batches

#accuracy
def accuracy(predicted, actual):
    predicted = predicted > 0.5
    actual = np.array(actual).reshape(actual.shape[0])
    predicted = np.array(predicted).reshape(predicted.shape[0])
    
    acc = (np.sum(actual == predicted)/len(actual)) * 100
    return acc

#normalize, scale btw 0 and 1
def normalize(x):
    x = x - np.amin(x)
    x = x/np.amax(x)
    return x

#calculates error of entire batch.
def calculateError(net, dataset):
    j = 0
    print(dataset.shape, dataset[0].shape)
    for data in dataset[0]:
        yPred = self.forwardPass(data[0])
        y = data[1].reshape((10,1)) ###added reshape
        costEx = cost(yPred, y)
        j += sum(costEx)
    '''
    yPred = net.forwardPass(dataset[0])
    y = dataset[1]
    costEx = cost(yPred, y) #error of single example.
    j = costEx.sum()
    '''
    
    return j/len(dataset[0]) #taking mean
    