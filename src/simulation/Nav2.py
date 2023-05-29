# Script para controlar a movimentação do robô por uma série de pontos utilizando a API do Nav2

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Seta pose inicial do robô
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = -2.00
    initial_pose.pose.position.y = -0.5
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    # Espera o Nav2 ficar ativo
    navigator.waitUntilNav2Active()

    # Define uma lista de poses para o robô percorrer
    goal_poses = []
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 0.004
    goal_pose1.pose.position.y = -2.02
    goal_pose1.pose.orientation.w = 0.707
    goal_pose1.pose.orientation.z = 0.707
    goal_poses.append(goal_pose1)

    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 2.03
    goal_pose2.pose.position.y = -0.91
    goal_pose2.pose.orientation.w = 0.707
    goal_pose2.pose.orientation.z = 0.707
    goal_poses.append(goal_pose2)

    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 0.6
    goal_pose3.pose.position.y = 0.57
    goal_pose3.pose.orientation.w = 0.707
    goal_pose3.pose.orientation.z = 0.707
    goal_poses.append(goal_pose3)

    goal_pose4 = PoseStamped()
    goal_pose4.header.frame_id = 'map'
    goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose4.pose.position.x = -1.81
    goal_pose4.pose.position.y = 0.52
    goal_pose4.pose.orientation.w = 0.707
    goal_pose4.pose.orientation.z = 0.707
    goal_poses.append(goal_pose4)

    # Envia a lista de poses para o Nav2
    navigator.goThroughPoses(goal_poses)

    i = 0

    # Enquanto o Nav2 não terminar a tarefa, imprime o tempo estimado para a tarefa terminar
    while not navigator.isTaskComplete():
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Estimated time of arrival: ' + '{0:.0f}'.format(
                  Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                  + ' seconds.')

            
            if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
                navigator.cancelTask()

            
            if Duration.from_msg(feedback.navigation_time) > Duration(seconds=35.0):
                pass

    # Imprime o resultado da tarefa
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    # Desliga o Nav2
    navigator.lifecycleShutdown()
    
    exit(0)


if __name__ == '__main__':
    main()