import sys
from . import dictionary, extract
import rclpy
from rclpy.node import Node
import os.path
import time
from custom_interfaces.srv import String


class KeyClientAsync(Node):
    def __init__(self):
        super().__init__('key_client_async')
        self.declare_parameter('dict_path', rclpy.Parameter.Type.STRING)
        dict_pather = self.get_parameter('dict_path')
        self.cli = self.create_client(String, 'key_listen')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.dicti = dictionary.Words(dict_pather.value)
        self.req = String.Request()
        self.creation = time.ctime(os.path.getctime('/home/csrobot/vosktest/input_saver/results/test.txt'))
        self.ready_to_send: bool = False
        #create timer here, bind timer_callback
        self.timer = self.create_timer(0.5, self.timer_callback)

    def send_request(self):
        self.ready_to_send = False
        self.ret = extract.clean_text(extract.get_text())
        self.split = self.ret.split(' ')
        self.match: list[str] = extract.match(self.split, self.dicti.get())
        res: str = ''
        for i in self.match:
            res=res+i+' '
        finalres: str = res[0:-1]
        if len(finalres) != 0:
            self.req.message = finalres
            self.get_logger().info(f'Sent {self.req.message}')
            self.future = self.cli.call_async(self.req)
            rclpy.spin_until_future_complete(self, self.future)
            return self.future.result()

    def timer_callback(self):
        # Required to exist for rclpy.ok() loop
        pass

def main(args=None):
    rclpy.init(args=args)
    minimal_client = KeyClientAsync()
    while rclpy.ok():
        # check here for new file, remove timer cb
        rclpy.spin_once(minimal_client)
        if minimal_client.creation != time.ctime(os.path.getctime('/home/csrobot/vosktest/input_saver/results/test.txt')):
            minimal_client.ready_to_send = True
            minimal_client.creation = time.ctime(os.path.getctime('/home/csrobot/vosktest/input_saver/results/test.txt'))
        if minimal_client.ready_to_send:
            response = minimal_client.send_request()
            minimal_client.ready_to_send=False
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
