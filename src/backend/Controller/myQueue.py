#!usr/bin/env python3

class queue(list):

    def __init__(self, sequence):
        super().__init__(item for item in sequence)

    def queue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)
    
    def clearQueue(self):
        self.clear()
    
    def showQueue(self):
        print(self)

    def isEmpty(self):
        if len(self) == 0:
            return True
        
    def first(self):
        return self[0]
    
    def __repr__(self):
        return f'Fila: {super().__repr__()}'