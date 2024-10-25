import rclpy
from custom_interfaces.srv import Stringer
from rclpy.action import ActionClient
from custom_interfaces.action import Huboaction
from rclpy.node import Node

class KeyService(Node):

    def __init__(self):
        super().__init__('key_service')
        self.srv = self.create_service(Stringer, 'key_listen', self.klisten_callback)
        self._action_client = ActionClient(self, Huboaction, 'hubo_as')
        self.goal_handle = None

    def klisten_callback(self, request, response):
        response.success = True
        self.msg = request.message
        self.get_logger().info(f"Received: {self.msg}")
        self.lst = self.msg.split()
        for ins in self.lst:
            if ins == 'walk':
                self.send_goal('walk')
            elif ins == 'drive':
                self.send_goal('drive')
            elif ins == 'rest':
                self.send_goal('rest')
            elif ins == 'transform':
                self.send_goal('transform')
            elif ins == 'stop':
                self.send_goal('stop')
        return response

    def send_goal(self, text):
        goal_msg = Huboaction.Goal()
        goal_msg.msg = text
        if text == 'stop':
            future = self.goal_handle.cancel_goal_async()
            future.add_done_callback(self.goal_canceled_callback)
        else:
            self._action_client.wait_for_server()
            self._send_goal_future = self._action_client.send_goal_async(
                goal_msg, feedback_callback=self.feedback_callback)

            self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_canceled_callback(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Cancelling of goal complete')
        else:
            self.get_logger().warning('Goal failed to cancel')

    def goal_response_callback(self, future):
        self.goal_handle = future.result()
        if not self.goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        self.get_logger().info('Goal accepted')

        self._get_result_future = self.goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.status))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            'Received feedback: {0}'.format(feedback.feedback))


def main(args=None):
    rclpy.init(args=args)

    key_service = KeyService()
    
    rclpy.spin(key_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
