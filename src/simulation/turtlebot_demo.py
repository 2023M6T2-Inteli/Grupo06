

# Importa bibliotecas
import rclpy

from MissionControl import MissionControl
from BotController import BotController  

def main(args=None):
    rclpy.init(args=args)
    mc = MissionControl()
    tc = BotController(mission_control=mc)
    rclpy.spin(tc)
    tc.destroy_node()

if __name__ == "__main__":
    main()