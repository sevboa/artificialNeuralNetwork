class BaseNeuron:
    def __init__(self):
        self.SignalPower = int()
        self.Activated = bool()
        self.Weight = float()
        self.DendriteCount = int()
        self.ConnectedNeurons = list()
    
    def setDendriteCount(self, dendriteCount):
        self.DendriteCount = dendriteCount
    
    def getWeight(self):
        return self.Weight
    
    def setWeight(self, weight):
        self.Weight = self.Weight + weight
        print('set weight ' + str(weight))
            
    def activation(self):
        print(self.SignalPower/self.DendriteCount, self.Weight)
        if (self.SignalPower/self.DendriteCount >= self.Weight):
            self.Activated = True
            for neuron in self.ConnectedNeurons:
                neuron.useDendrite(1)
            
    def useDendrite(self, signalPower):
        self.SignalPower = self.SignalPower + signalPower
    
    def connectNeuron(self, neuron):
        self.ConnectedNeurons.append(neuron)
    