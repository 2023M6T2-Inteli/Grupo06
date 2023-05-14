from turtlesim.msg import Pose as TPose

# Define a classe Rotation, que representa o quanto o robô precisa rotacionar
class Rotation(TPose):

    def __init__(self, theta=0.0):
        super().__init__(x=0.0, y=0.0, theta=theta)
        self.rotated = False
        
    def __repr__(self):
        return f"(theta={self.theta:.2f})"
    
    def __eq__(self, other):
        return abs(self.theta - other.theta) <= 0.05