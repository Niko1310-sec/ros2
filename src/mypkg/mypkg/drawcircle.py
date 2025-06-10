#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("drawcircle") #node name
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) # topic name and queue size
        self.timer = self.create_timer(1.0, self.send_vel_command)
        self.get_logger().info("Draw circle node has been started")

    def send_vel_command(self): # specifying what the topic has to do
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg) # publishing data to the node

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()