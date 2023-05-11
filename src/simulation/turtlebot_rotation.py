import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from turtlesim.msg import Pose as TPose
import math

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
        return abs(self.x - other.x) <= MAX_DIFF and abs(self.y - other.y) <= MAX_DIFF
    
class Rotation(TPose):

    def __init__(self, theta=0.0):
        super().__init__(x=0.0, y=0.0, theta=theta)
        
    def __repr__(self):
        return f"(theta={self.theta:.2f})"
    
    def __eq__(self, other):
        return abs(self.theta - other.theta) <= MAX_DIFF
    

class BotController(Node):
    def __init__(self, control_period=0.02):
        super().__init__("bot_controller")

        self.initiated = False
        self.setpoint = Pose()
        self.pose = Pose()
        self.theta= Rotation()
        self.setpoint_rotation = Rotation()
        self.current_rotation = Rotation()
        
        self.control_timer = self.create_timer(
            timer_period_sec=control_period, 
            callback=self.control_callback
        )

        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic="odom",
            callback=self.pose_callback,
            qos_profile=10
        )
        self.publisher = self.create_publisher(
            msg_type=Twist, 
            topic="cmd_vel", 
            qos_profile=10
        )

    def control_callback(self): 
        if not self.initiated:
            self.get_logger().info("Aguardando pose...")
            return
        
        msg = Twist()

        if self.current_rotation == self.setpoint_rotation:
            msg.angular.z = 0.0
            self.get_logger().info(f"Donatello chegou em {self.setpoint}")
            self.publisher.publish(msg)
            exit()
        else:
            offset = self.setpoint_rotation.theta - self.current_rotation.theta
            if abs(offset) > MAX_DIFF:
                msg.angular.z = 0.5 if offset > 0 else -0.5
        
        self.publisher.publish(msg)

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        self.pose = Pose(x=x, y=y, theta=theta)

        if not self.initiated:
            self.initiated = True
            self.setpoint = Pose(self.pose.x + 10.0, + self.pose.y + -5.0)
            print(f"pose inicial: {self.pose}")
            self.get_logger().info(f"Setpoint: {self.setpoint}")

        self.current_rotation = Rotation(theta=theta)

        if self.setpoint == Pose(0.0,0.0):
            self.theta = Rotation(theta=0.0) 
        else:
            self.theta= Rotation(theta=math.atan2(self.setpoint.y - self.pose.y, self.setpoint.x - self.pose.x))

        self.relative_translation = Pose(x=self.setpoint.x - self.pose.x, y=self.setpoint.y - self.pose.y)

        if self.relative_translation.x >= 0 and self.relative_translation.y >=0:
            self.setpoint_rotation = Rotation(theta=-(math.pi/2 - abs(self.theta.theta)))

        elif self.relative_translation.x >=0 and self.relative_translation.y <= 0:
            self.setpoint_rotation = Rotation(theta=-(math.pi/2 + abs(self.theta.theta)))

        elif self.relative_translation.x <=0 and self.relative_translation.y <= 0:
            self.setpoint_rotation = Rotation(theta=-self.theta.theta)
        else:
            self.setpoint_rotation = Rotation(theta= -(math.pi/2 - abs(self.theta.theta)))


def main(args=None):
    rclpy.init(args=args)
    tc = BotController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()