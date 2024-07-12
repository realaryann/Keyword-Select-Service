import rclpy
from custom_interfaces.srv import String
from rclpy.node import Node

class KeyService(Node):

    def __init__(self):
        super().__init__('key_service')
        self.srv = self.create_service(String, 'key_listen', self.klisten_callback)

    def klisten_callback(self, request, response):
        response.success = True
        self.msg = request.message
        self.lst = self.msg.split()
        for ins in self.lst:
            if ins == 'walk':
                self.walk()
            elif ins == 'wheel':
                self.wheel()
            elif ins == 'rest':
                self.rest()
            elif ins == 'transform':
                self.transform()
        return response

    def walk(self):
        return 

    def wheel(self):
        return

    def rest(self):
        return

    def transform(self):
        return

def main(args=None):
    rclpy.init(args=args)

    key_service = KeyService()

    rclpy.spin(key_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()