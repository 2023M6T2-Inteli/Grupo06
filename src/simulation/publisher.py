import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion

MAX_DIFF = 0.1

class Pose(Odometry):
    def __init__(self, x = 0.0, y = 0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
    
    def __repr__(self):
        return f"x={self.x}, y={self.y}"
    
    def __add__(self, other):
        return Pose(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pose(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return abs(self.x - other.x) < MAX_DIFF \
            and abs(self.y - other.y) < MAX_DIFF

class TurtleController(Node):

    def __init__(self, control_period=0.02): 
        super().__init__("turtle_controller")

        self.initiated = False

        self.pose = Pose(x=0, y=0, theta=0)

        self.setpoint = Pose(x=0, y=0, theta=0)
        
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

        if self.pose == self.setpoint:
            self.get_logger().info("Chegou no destino!")
            msg.linear.x = 0.0
            exit()
        
        x_diff = self.setpoint.x - self.pose.x
        y_diff = self.setpoint.y - self.pose.y

        if abs(x_diff) > MAX_DIFF:
            msg.linear.x = 1.0 if x_diff > 0 else -1.0

        if abs(y_diff) > MAX_DIFF:
            msg.linear.y = 1.0 if y_diff > 0 else -1.0
        
        self.publisher.publish(msg)

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])

        self.pose = Pose(x=x, y=y, theta=theta)

        if not self.initiated:
            self.setpoint = self.pose + Pose(x=1, y=1)
            self.initiated = True

        self.get_logger().info(f"x={x}, y={y}, theta={theta}")

def main(args=None):
    rclpy.init(args=args)
    tc = TurtleController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
