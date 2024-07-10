import rclpy
from . import dictionary, extract
from rclpy.node import Node
from std_msgs.msg import String


class KeyPublisher(Node):

    def __init__(self):
        super().__init__('key_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.dicti = dictionary.Words()

    def timer_callback(self):
        self.ret = extract.clean_text(extract.get_text())
        self.split = self.ret.split(' ')
        self.match = extract.match(self.split, self.dicti.get())
        msg = String()
        res=''
        for i in self.match:
            res=res+i+' '
        finalres = res[0:-1]
        msg.data = finalres
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    key_publisher = KeyPublisher()

    rclpy.spin(key_publisher)

    key_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()