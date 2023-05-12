import rclpy
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('add_two_ints_client')

    client = node.create_client(AddTwoInts, 'add_two_ints')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')
    
    request = AddTwoInts.Request()
    request.a = 2
    request.b = 3
    
    future = client.call_async(request)

    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        response = future.result()
        node.get_logger().info('Result of add_two_ints: %d' % (response.sum))
    else:
        node.get_logger().info('Service call failed')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
