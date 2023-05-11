
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose as TPose
from collections import deque

MAX_DIFF = 0.1

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
        print(f"Comparando {self} com {other}")
        return abs(self.x - other.x) <= MAX_DIFF

class MissionControl(deque):
    
    def __init__(self):
        super().__init__()
        self.enqueue(Pose(x=4.54))
        self.enqueue(Pose(x=7.54))
        self.enqueue(Pose(x=4.54))
        
    def enqueue(self, x):
        """Método para adicionar novos pontos ao fim da fila."""
        super().append(x)
    
    def dequeue(self):
        """Método para retirar pontos do começo da fila."""
        return super().popleft()


class TurtleController(Node):
    
    def __init__(self, control_period=0.02, queue=MissionControl()):
        super().__init__('turtle_controller')

        self.initiated = False

        self.pose = Pose()
        self.setpoint = Pose()
        self.queue = queue

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic="/turtle1/cmd_vel",
            qos_profile=10
        )
        self.subscription = self.create_subscription(
            msg_type=Pose,
            topic="/turtle1/pose",
            callback=self.pose_callback,
            qos_profile=10
        )

        self.control_timer = self.create_timer(
                timer_period_sec=control_period,
                callback=self.control_callback
        )

    def update_setpoint(self):
        """ Método responsável por buscar um novo setpoint na fila"""
        try:
            self.setpoint = self.queue.dequeue()
            self.get_logger().info(f"Mbpappé chegou em {self.pose}, \
                                   andando para {self.setpoint}")
        except IndexError:
            self.get_logger().info(f"Fim da jornada!")
            exit()

    def control_callback(self):

        if not self.initiated:
            self.get_logger().info("Aguardando primeira pose...")
            return
        msg = Twist()
        x_diff = self.setpoint.x - self.pose.x

        #self.get_logger().info(f"x_diff: {x_diff}")
        #self.get_logger().info(f"Pose: {self.pose}")

        if self.pose == self.setpoint:
            self.get_logger().info("To aqui")
            msg.linear.x = 0.0
            self.get_logger().info(f"Mbappé chegou em {self.setpoint}")
            self.update_setpoint()
     
        if abs(x_diff) > MAX_DIFF:
            self.get_logger().info(f"Distância para o setpoint: {x_diff}")
            msg.linear.x = 0.5 if x_diff > 0 else -0.5
        
        self.publisher.publish(msg)
        
    def pose_callback(self, msg):

        self.pose = Pose(x=msg.x, y=msg.y, theta=msg.theta)

        if not self.initiated:
            self.initiated = True
            self.get_logger().info(f"Primeira pose recebida: {self.pose}")
            self.update_setpoint()
            self.get_logger().info(f"Setpoint: {self.setpoint}")


def main(args=None):
    rclpy.init(args=args)
    tc = TurtleController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()