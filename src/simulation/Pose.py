from max_diffs import MAX_DIFF
from turtlesim.msg import Pose as TPose

# Define a classe Pose, que representa uma posição no mundo
class Pose(TPose):

    def __init__(self, x=0.0, y=0.0, theta=0.0):
        super().__init__(x=x, y=y, theta=theta)
        
    def __repr__(self):
        return f"(x={self.x:.2f}, y={self.y:.2f}, theta={self.theta:.2f})"
    
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __eq__(self, other):
        return abs(self.x - other.x) <= MAX_DIFF and abs(self.y - other.y) <= MAX_DIFF