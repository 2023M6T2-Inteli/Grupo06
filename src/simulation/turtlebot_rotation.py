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
        self.rotated = False
        
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
        self.setpoint_translation = 0.0
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

        if not self.setpoint_rotation.rotated:
            if self.current_rotation == self.setpoint_rotation:
                msg.angular.z = 0.0
                self.get_logger().info(f"Donatello rodou o suficiente")
                self.setpoint_rotation.rotated = True
                print(f"final_rotation: {self.current_rotation}")
            else:
                offset = self.setpoint_rotation.theta - self.current_rotation.theta
                if abs(offset) > 0.05:
                    msg.angular.z = 0.5 if offset > 0 else -0.5
        else:
            if self.pose == self.setpoint:
                msg.linear.x = 0.0
                self.get_logger().info(f"Donatello chegou ao destino")
                self.publisher.publish(msg)
                exit()
            else:
                offset = self.setpoint_rotation.theta - self.current_rotation.theta
                print(f"offset: {offset}")
                if abs(offset) > 0.05:
                    msg.angular.z = 0.5 if offset > 0 else -0.5
                else:
                    msg.angular.z = 0.0
                self.relative_vector = Pose(x=self.setpoint.x - self.pose.x, y=self.setpoint.y - self.pose.y)
                print(f"setpoint: {self.setpoint}, pose: {self.pose}, relative_vector: {self.relative_vector}")
                self.relative_translation = math.sqrt(self.relative_vector.x**2 + self.relative_vector.y**2)
                print(f"relative_tranlation: {self.relative_translation}")
                if self.relative_translation > MAX_DIFF:
                    msg.linear.x = 0.5 if self.relative_translation > 0 else -0.5

        
        self.publisher.publish(msg)

    def update_setpoint(self):
        self.setpoint = Pose(self.pose.x + -1.0, + self.pose.y + 1.0)

        if self.setpoint == Pose(0.0,0.0):
            self.theta = Rotation(theta=0.0) 
        else:
            self.theta= Rotation(theta=math.atan2(self.setpoint.y - self.pose.y, self.setpoint.x - self.pose.x))
            print(f"theta: {self.theta}")

        self.relative_vector = Pose(x=self.setpoint.x - self.pose.x, y=self.setpoint.y - self.pose.y)
        self.relative_translation = math.sqrt(self.relative_vector.x**2 + self.relative_vector.y**2)

        if self.relative_vector.x >= 0 and self.relative_vector.y >=0:
            self.setpoint_rotation = Rotation(theta=abs(self.theta.theta))

        elif self.relative_vector.x >=0 and self.relative_vector.y <= 0:
            self.setpoint_rotation = Rotation(theta=-abs(self.theta.theta))

        elif self.relative_vector.x <=0 and self.relative_vector.y <= 0:
            self.setpoint_rotation = Rotation(theta=-abs(self.theta.theta))
            print(f"setpoint_rotation: {self.setpoint_rotation}")
        else:
            self.setpoint_rotation = Rotation(theta=abs(self.theta.theta))

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        self.pose = Pose(x=x, y=y, theta=theta)
        self.current_rotation = Rotation(theta=self.pose.theta)

        if not self.initiated:
            self.initiated = True
            print(f"pose inicial: {self.pose}")
            self.update_setpoint()
            self.get_logger().info(f"Setpoint: {self.setpoint}")


def main(args=None):
    rclpy.init(args=args)
    tc = BotController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()