import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import ChangeState
from lifecycle_msgs.msg import Transition

class LifecycleController(Node):
    def __init__(self):
        super().__init__("lifecycle_controller")

        self.client = self.create_client(ChangeState, '/lifecyclenode/change_state')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for the lifecycle node to respond...")

        self.send_transition(Transition.TRANSITION_CONFIGURE)
        self.send_transition(Transition.TRANSITION_ACTIVATE)

    def send_transition(self, transition_id):
        request = ChangeState.Request()
        request.transition.id = transition_id

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        result = future.result()

        if result.success:
            self.get_logger().info(f"Transition {transition_id} succeeded")
        else:
            self.get_logger().error("Transition failed")

def main(args=None):
    rclpy.init(args=args)
    node = LifecycleController()
    rclpy.spin_once(node)
    rclpy.shutdown()
