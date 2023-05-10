from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from Pose import Pose
MAX_DIFF = 0.5



class BotController(Node):
    def __init__(self, mission_control, control_period=0.02):
        super().__init__("mission_controller")

        self.initiated = False

        self.mission_control = mission_control

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
            msg.linear.y = 0.0
            self.update_setpoint()
        
        x_diff = self.setpoint.x - self.pose.x
        y_diff = self.setpoint.y - self.pose.y

        if abs(x_diff) > MAX_DIFF:
            msg.linear.x = 1.0 if x_diff > 0 else -1.0

        if abs(y_diff) > MAX_DIFF:
            msg.linear.y = 1.0 if y_diff > 0 else -1.0
        
        self.publisher.publish(msg)

    def update_setpoint(self):
        """ Método responsável por buscar um novo setpoint na fila"""
        try:
            self.setpoint = self.pose + self.mission_control.dequeue()
            self.get_logger().info(f"Mbpappé chegou em {self.pose}, \
                                   andando para {self.setpoint}")
        except IndexError:
            self.get_logger().info(f"Fim da jornada!")
            exit()

    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])

        self.pose = Pose(x=x, y=y, theta=theta)

        if not self.initiated:
            self.update_setpoint()
            self.initiated = True