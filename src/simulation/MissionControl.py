from Pose import Pose
from collections import deque

# Define a classe MissionControl, que representa a fila de pontos a serem seguidos
class MissionControl(deque):

    # Define a sequência de pontos para cada formato disponível
    shapes = {
        "square": [
            Pose(1.0, 1.0), Pose(1.0, -1.0), Pose(-1.0, -1.0), Pose(-1.0, 1.0), Pose(1.0, 1.0)
        ],
        "g": [
            Pose(-1.0, 1.0), Pose(-2.0, 0.0), Pose(-1.0, -1.0), Pose(0.0, -0.3), Pose(-0.5, -0.45)
        ],
        '': [Pose(0.0, 0.0)]
    }

    def __init__(self):
        super().__init__()
        
    def enqueue(self, x):
        super().append(x)
    
    def dequeue(self):
        return super().popleft()
    
    # Define a função que preenche a fila com os pontos do formato selecionado
    def load_shape(self, shape):
        super().clear()
        for pose in MissionControl.shapes[shape]:
            self.enqueue(pose)
    
    # Define a função que preenche a fila com um ponto específico
    def load_point(self, x, y):
        super().clear()
        self.enqueue(Pose(x, y))