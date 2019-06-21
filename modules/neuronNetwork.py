import random

from modules.internalNeuron import InternalNeuron
from modules.outputNeuron import OutputNeuron
from modules.inputNeuron import InputNeuron

class NeuronNetwork:
    Neurons = dict()
    def __init__(self, dendriteCount, axonCount, randomSeed = 5):
        self.DendriteCount = dendriteCount
        self.AxonCount = axonCount
        self.Rows = list()
        
        random.seed(randomSeed)
        
        self.addInputRowNeurons()
        
    def build(self):
        self.addOutputRowNeurons()
        
        rowNumber = int(0)
        for row in self.Rows:
            print(2)
            for neuron in row:
                print(3)
                print(neuron.__dict__)
                neuron.setWeight(random.random())
                if rowNumber > 0:
                    dendriteCount = len(self.Rows[rowNumber - 1])
                    neuron.setDendriteCount(dendriteCount)
                    for prevNeuron in self.Rows[rowNumber - 1]:
                        prevNeuron.connectNeuron(neuron)
                else:
                    neuron.setDendriteCount(1)
            rowNumber = rowNumber + 1
        print('builded')
                
    def printNeuronsWeight(self):
        print(' neurons weight:')
        for row in self.Rows:
            for neuron in row:
                print(neuron.getWeight(), end = ' ')
            print()
            
    def sendData(self, inputData):
        if len(inputData) == len(self.Rows[0]):
            valueNumber = int()
            for inputNeuron in self.Rows[0]:
                inputNeuron.useDendrite(inputData[valueNumber])
                valueNumber = valueNumber + 1
        self.activate()
                    
    def activate(self):
        for row in self.Rows:
            print(row)
            for neuron in row:
                neuron.activation()
                print(neuron.Activated)
    
    def addRowNeurons(self, NeuronClass, neuronCount):
        row = list()
        while len(row) < neuronCount:
            neuron = NeuronClass()
            print(dir(neuron))
            row.append(neuron)
        self.Rows.append(row)
    
    def addInputRowNeurons(self):
        self.addRowNeurons(InputNeuron, self.DendriteCount)
    
    def addInternalRowNeurons(self, neuronCount):
        self.addRowNeurons(InternalNeuron, neuronCount)
        
    def addOutputRowNeurons(self):
        self.addRowNeurons(OutputNeuron, self.AxonCount)

   
    