from collections import deque 
import csv
from Pose import Pose


class MissionControl(deque):

    def __init__(self, csv_file="pontos.csv"): 
        super().__init__()

        with open(csv_file) as csv_file:
            # Se você criar o arquivo em um excel BR, vai precisar mudar o delimitador
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                new_pose = Pose()
                new_pose.x, new_pose.y = [float(x) for x in row]
                self.enqueue(new_pose)
            print(self)

    def enqueue(self, x):
        """Método para adicionar novos pontos ao fim da fila."""
        super().append(x)
    
    def dequeue(self):
        """Método para retirar pontos do começo da fila."""
        return super().popleft()