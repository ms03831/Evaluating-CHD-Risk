import numpy as np

#sigmoid(z)
def sigmoid(z): 
    return 1/(1+np.exp(-z)) 

#MSE
def cost(yPred, y): 
    return 0.5*(yPred-y)**2

#derivative of cost 
def derivateCost(yPred, y): 
    return yPred - y

#iterator
def dataIter(batchSize, data):
    random.shuffle(data)
    batches = []
    for i in range(0, data.shape[0], batchSize):
        batches.append(data[i:i+batchSize])
    return batches

#accuracy
def accuracy(net, actual, predicted):
    accuracy = np.sum(actual == predicted).mean() * 100
    return accuracy

#normalize, scale btw 0 and 1
def normalize(x):
    x = x - np.amin(x)
    x = x/np.amax(x)
    return x

#calculates error of entire batch.
def calculateError(net, dataset):
    j = 0
    for data in dataset:
        yPred = net.forwardPass(data[0])
        y = data[1]
        costEx = cost(yPred, y) #error of single example.
        j += sum(costEx)
    return j/len(trainData) #taking mean
    