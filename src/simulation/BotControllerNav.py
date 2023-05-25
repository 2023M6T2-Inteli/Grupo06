# Este script cria um nó de ROS2 para controlar o movimento do robô.
# Ele permite criar filas de pontos para o robô seguir, e também permite
# enviar comandos de formato ou posição para o robô seguir a partir de um servidor.
# Para isso, foram criadas funções de transformação de base, que traduzem coordenadas
# absolutas do mundo para coordenadas relativas ao robô, isto é, uma rotação no
# eixo z do robô e uma translação no eixo x do robô.
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import rclpy
from Pose import Pose

# Define a classe BotController, que representa o nó de controle do robô
class BotController(Node):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    # Inicializa o nó com período de controle de 0.05s e uma fila vazia
    def __init__(self, control_period=0.05):
        super().__init__("bot_controller")
        print('oi')
        self.current_pose = Pose()
        # Cria um assinante para receber a pose do robô
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic="odom",
            callback=self.pose_callback,
            qos_profile=10
        )
    # Callback para receber pose atual
    def pose_callback(self, msg):
            print("aqui")
            # Decompõe a mensagem de pose em x, y e theta
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            z = msg.pose.pose.position.z
            ang = msg.pose.pose.orientation
            
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
            # Atualiza a pose e rotação atuais
            self.current_pose = Pose(x=x, y=y, theta=theta)
            print(x, y, ang.z, ang.w)
def main():
    rclpy.init()
    tc = BotController()
    rclpy.spin(tc)
if __name__ == "__main__":
    main()