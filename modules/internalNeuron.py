from modules.baseNeuron import BaseNeuron

class InternalNeuron(BaseNeuron):
    def __init__(self):
        super().__init__()
        self.DendriteCount = 1
        return