import random

from modules.inputNeuron import InputNeuron
from modules.neuronNetwork import NeuronNetwork

random.seed(847633)

Neuron = InputNeuron()
Neuron.setWeight(random.randrange(0,2))
Neuron.useDendrite(0)
print(Neuron.getWeight())
print(Neuron.activation())

NeuronNetwork = NeuronNetwork(4,4)
NeuronNetwork.addInternalRowNeurons(8)
NeuronNetwork.addInternalRowNeurons(8)
NeuronNetwork.addInternalRowNeurons(8)
NeuronNetwork.addInternalRowNeurons(8)
NeuronNetwork.build()
NeuronNetwork.printNeuronsWeight()
NeuronNetwork.sendData([1,0,1,0])
