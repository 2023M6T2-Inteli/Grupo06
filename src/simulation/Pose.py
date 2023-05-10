from nav_msgs.msg import Odometry
import numpy as np


MAX_DIFF = 0.5

class Pose(Odometry):
    def __init__(self, x = 0.0, y = 0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
    
    def __repr__(self):
        return f"x={self.x}, y={self.y}, theta={self.theta}"
    
    def __add__(self, other):
        return Pose(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pose(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return abs(self.x - other.x) < MAX_DIFF \
            and abs(self.y - other.y) < MAX_DIFF

