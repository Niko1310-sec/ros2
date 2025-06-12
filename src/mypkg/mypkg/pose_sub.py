#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Posesub(Node):

    def __init__(self):
        super().__init__("pose_sub")
        self.pose_sub = self.create_subscription(Pose , "/turtle1/pose", self.pose_callback, 10 )

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(Pose))

def main(args=None):
    rclpy.init(args=args)
    node = Posesub()
    rclpy.spin(node)
    rclpy.shutdown()
