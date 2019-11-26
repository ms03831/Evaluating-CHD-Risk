import numpy as np
from matplotlib import pyplot as plt 
from helperFunctions import *

trainError = []
trainAccuracy = []
testError = []

class MyNeuralNet:
    def __init__(self, layerArray):
        
        """ 
        layerArray: 
            array of dimensions of layers. 
            size of layerArray is the number of layers in our network
        """
            
        self.layers = layerArray #layes in our network
        self.B = [] #bias matrix
        self.W = [] #weights matrix
        self.input = None 

        for layerNum in range(1, len(layerArray)): #1st layer is input so we exclude that
            biasVector = np.zeros((layerArray[layerNum], 1)) #bias zero initialized 
            self.B.append(biasVector)
            weightsMatrix = np.random.normal(loc = 0, scale = 1, size = (layerArray[layerNum], layerArray[layerNum-1])) #weights initialized with normal dist
            self.W.append(weightsMatrix)
            
    
    def netSize(self):
        """ 
        number of layers in the network excluding the input layer
        """    
        return len(self.layers) - 1
    
    def activateLayer(self, z):
        """
        applies activation function to the layer z. 
        activation : sigmiod
        """
        activatedLayer = sigmoid(z)
        return activatedLayer
    
    def derivatieActivateLayer(self, z):
        """ 
        applies derivate of activation function to the layer z. 
        activation : sigmiod
        """
        z = np.array(z)
        sigmoid = self.activateLayer(z)
        return sigmoid*(1-sigmoid)


    def forwardPass(self, layer, func = 0):
        """
        passes through the network, calculates linear score and then applies sigmoid to it.
        """
        for i in range(self.netSize()):
            layer = np.dot(self.W[i], layer) + self.B[i]
            layer = self.activateLayer(layer, func)
        return layer
    
    def backPropagate(self, x, y):
        """
        Backpropagates through the network to calculate gradients. 
        """

        #dW and dB hold the gradients of cost wrt. weights and biases. initilially zero
        dW = []
        dB = []
        for i in range(self.netSize()):
            dW.append(np.zeros(self.W[i].shape))
            dB.append(np.zeros(self.B[i].shape))

        outputLayers = [] #Z's
        activeOutputLayers = [] #Sigmoid of Z's or g(Z)

        activeOutput = x #input layer 
        activeOutputLayers.append(activeOutput)
        
        for b,w in zip(self.B, self.W):
            output = np.dot(w, activeOutput) + b
            outputLayers.append(output)
            activeOutput = self.activateLayer(output, func)
            activeOutputLayers.append(activeOutput)
        
        outputLayers = np.array(outputLayers)
        activeOutputLayers = np.array(activeOutputLayers)
        n = self.netSize()
        dZ = derivateCost(activeOutput, y) * self.derivatieActivateLayer(output, func)
        dW[n-1] = np.dot(dZ, activeOutputLayers[-2].T)
        dB[n-1] = dZ
        for l in range(n-1):
            dZ = np.dot(self.W[n-1-l].T, dZ) * self.derivatieActivateLayer(outputLayers[n-2-l], func)
            dB[l] = dZ
            dW[l] = np.dot(dZ , activeOutputLayers[max(0,n-3-l)].T)

        dB = np.array(dB)
        dW = np.array(dW)
        return (np.array(dB), np.array(dW))
   

    def train(self, train, test, epochs, batchSize, learningRate, validation = None):
        """
        Trains the network using mini-batch gradient descent.
        """

        for i in range(epochs):
            for batch in dataIter(batchSize, train):
                xBatch, yBatch = batch[:, :-1], batch[:, -1]
                dW = []
                dB = []

                #initialize gradients
                for j in range(self.netSize()):
                    dW.append(np.zeros(self.W[j].shape))
                    dB.append(np.zeros(self.B[j].shape))

                for x, y in zip(xBatch, yBatch):

                    #obtain gradients by backpropagating
                    gradB, gradW = self.backPropagate(x, y, func)
                    n = self.netSize()

                    #summing weights and biases for all examples in the mini batch
                    dW = [w + gradw for w, gradw in zip(dW, gradW)]
                    dB = [b + gradb for b, gradb in zip(dB, gradB)]

                for j in range(self.netSize()):
                    self.W[j] = self.W[j] - (learningRate/batchSize)*dW[j]
                    self.B[j] = self.B[j] - (learningRate/batchSize)*dB[j]
            
            trainError.append(calculateError(self, train))
            trainAccuracy.append(accuracy1)
            testError.append(calculateError(self, test))
