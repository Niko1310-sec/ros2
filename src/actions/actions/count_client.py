import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle
from custom_interfaces.action import CountUntil

class CountUntilClient(Node):
    def __init__(self):
        super().__init__("count_until_client")
        self.count_until_client = ActionClient(
            self,
            CountUntil,
            "count_until",
            
        )
    def send_goal(self, target_number, period_number):
        # Wait for the server
        self.count_until_client.wait_for_server()

        # Create a goal
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period_number

        # Send the goal
        self.get_logger().info("Sending the Goal")
        self.count_until_client.send_goal_async(goal).add_done_callback(self.get_response_callback)

        # Goal accepted or not
    def get_response_callback(self, future):
        self.goal_handle : ClientGoalHandle = future.result()
        if self.goal_handle.accepted:
            self.goal_handle.get_result_async().add_done_callback(self.goal_result_callback)

        # If the Goal is accepted request result
    def goal_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("Result : "+ str(result.reached_number))        
            
def main(args=None):
    rclpy.init(args=args)
    node = CountUntilClient()
    node.send_goal(8, 1.0)
    rclpy.spin(node)
    rclpy.shutdown()