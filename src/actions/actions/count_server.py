import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from custom_interfaces.action import CountUntil

class CountuntilServer(Node):
    def __init__(self):
        super().__init__("Countuntil")
        self.count_until_server = ActionServer(self, CountUntil, "count_until", execute_callback=self.execute_callback)
        self.get_logger().info("Action Server has been started")

    def execute_callback(self, goal_handle: ServerGoalHandle):
        # Get a request from a goal
        target_number = goal_handle.request.target_number
        peroid = goal_handle.request.period

        feedback_msg = CountUntil.Feedback()

        # Execute the Goal
        self.get_logger().info("Executing the Goal")
        Counter = 0
        for i in range(target_number):
            Counter += 1
            self.get_logger().info(str(Counter))
            time.sleep(peroid)

        feedback_msg.current_number = Counter
        goal_handle.publish_feedback(feedback_msg)
        
        # Once done, set the goal_handle to succeed
        goal_handle.succeed()    

        # send the result
        result = CountUntil.Result()
        result.reached_number = Counter
        return result


def main(args=None):
    rclpy.init(args=args)
    node = CountuntilServer()
    rclpy.spin(node)
    rclpy.shutdown()