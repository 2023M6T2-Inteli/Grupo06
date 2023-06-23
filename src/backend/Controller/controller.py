#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import math
from myQueue import queue
import time

class gazebo_node(Node):

    def __init__(self):
        super().__init__('gazebo_controller')
        self.get_logger().info("Initializing gazebo_controller node...")

        self.fila = queue([])

        self.odometry_subscriber = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.odometry_callback,
            qos_profile=10
        )
        self.velocity_publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10
        )
        # create a timer to calculation the distance and the angle difference between the robot and the goal
        self.pose = [0, 0, 0]
        self.relativePose = [0, 0]
        self.isMoving = False
        self.minDistance = 10000
        self.proportionalDistance = 1
        self.proportionalAngle = 0.2
        self.safeStop = True
        self.stopAll()


    def rota_padrão(self):
        print("Aperte 1 para rodar o trajeto padrão ou 2 para personalizar um trajeto!")
        opcao = input()
        while opcao != "1" and opcao != "2":
            print("Opção inválida, digite novamente!")
            opcao = input()
        if opcao == "1":
            self.fila.queue([3,4])
            self.fila.queue([2,-5])
            self.fila.queue([5,-5])
        else:
            print("Digite a quantidade de pontos que deseja percorrer: ")
            qtd = int(input())
            for i in range(qtd):
                print("Digite o ponto que deseja percorrer: ")
                print("x: ")
                x = float(input())
                print("y: ")
                y = float(input())
                self.fila.queue([x,y])
        self.fila.showQueue()

    def odometry_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        orientation = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        pose = [round(x, 2), round(y, 2), round(theta, 2)]
        print("Posição atual:", pose)
        self.pose = pose
        if self.fila.isEmpty():
            self.get_logger().info("Fila vazia, aperte Ctrl+C para sair")
        else:
            self.calculation(self.fila.first())

    def calculation(self, track):
        if self.isMoving == True:
            # only update the distance
            distance = math.sqrt(((track[0] - self.pose[0]) ** 2) + ((track[1] - self.pose[1]) ** 2))
            self.relativePose[0] = round(distance,2)
            print(self.relativePose)
        else:
            # calculate the distance between the robot and the goal
            distance = math.sqrt(((track[0] - self.pose[0]) ** 2) + ((track[1] - self.pose[1]) ** 2))
            # calculate the angle between the robot and the goal
            angle = math.atan2(track[1] - self.pose[1], track[0] - self.pose[0])
            # calculate the angle difference between the robot and the goal
            angle_difference = angle - self.pose[2]
            # return the distance and the angle difference
            print("Distãncia linear/angular do objetivo:", [round(distance,2), round(angle_difference, 3)])
            self.relativePose[0] = round(distance,2)
            self.relativePose[1] = round(angle_difference, 3)
        # check if relativePose[0] is less than minDistance with a tolerance of 0.05 (inertia)
        if round(self.relativePose[0],1) < round(self.minDistance,1) + 0.05:
            self.minDistance = self.relativePose[0]
            print("Menor distância:", self.minDistance, "menor distancia relativa:" , self.relativePose[0])

        if self.relativePose[0]<1.0:
            self.proportionalDistance = self.relativePose[0]
            if self.relativePose[0] < 0.1:
                self.proportionalDistance = 0.1
        else:
            self.proportionalDistance = 1

        if abs(self.relativePose[1]) < 0.5:
            if abs(self.relativePose[1]) > 0.45 and self.safeStop == True:
                self.stopAll()
                time.sleep(2)
                self.safeStop = False
            if self.relativePose[1] < 0.50:
                self.proportionalAngle = 0.0025
            else:
                self.proportionalAngle = 0.01
        else:
            self.proportionalAngle = 0.2

        self.move()

        
    def move(self):
        if self.relativePose[0] > 0.1 and self.minDistance == self.relativePose[0]:
            if self.relativePose[1] < 0.01 and self.relativePose[1] > -0.01:
                # create a Twist message to move the robot
                print("movendo teoricamente")
                vel_msg = Twist()
                vel_msg.linear.x = 0.2 * self.proportionalDistance
                vel_msg.angular.z = 0.0
                self.velocity_publisher.publish(vel_msg)
                self.isMoving = True
                self.minDistance = self.relativePose[0]
                print("aqui")
            else:
                # create a Twist message to rotate the robot
                print("Rotacionando para encontrar o melhor trajeto...")
                vel_msg = Twist()
                vel_msg.linear.x = 0.0
                vel_msg.angular.z = 10 * self.proportionalAngle
                self.velocity_publisher.publish(vel_msg)
                if self.relativePose[1] < 0.01 and self.relativePose[1] > -0.01:
                    self.stopAll()
                    print("aqui2")
        else:
            print("cabou")
            self.safeStop = True
            self.isMoving = False
            self.rightAngle = False
            self.minDistance = 10000
            vel_msg = Twist()
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0
            self.velocity_publisher.publish(vel_msg)
            self.fila.dequeue()
            self.fila.showQueue()
            time.sleep(2) # Aguarda 1 segundos para o robô parar completamente antes de começar a calcular a distância novamente

    def stopAll(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
        self.velocity_publisher.publish(vel_msg)           




def main(args=None):
    rclpy.init(args=args)
    node = gazebo_node()
    node.rota_padrão()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()