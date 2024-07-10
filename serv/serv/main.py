import rclpy
from custom_interfaces.srv import String
from rclpy.node import Node

class KeyService(Node):

    def __init__(self):
        super().__init__('key_service')
        self.srv = self.create_service(String, 'key_listen', self.klisten_callback)

    def klisten_callback(self, request, response):
        response.success = True
        self.get_logger().info(f'Incoming request: {request.message}' )
        return response


def main(args=None):
    rclpy.init(args=args)

    key_service = KeyService()

    rclpy.spin(key_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()