import rclpy
from rclpy.node import node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__()