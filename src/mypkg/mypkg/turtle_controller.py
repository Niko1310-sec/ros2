#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_sub = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.previous_x_ = 0.0
        self.get_logger().info('the turtle controller has been started')
        
    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 1.0
        else:    
            cmd.linear.x = 3.0
            cmd.angular.z = 0.0
        self.cmd_vel.publish(cmd)

        if pose.x > 5.5 and self.previous_x_ <= 5.5:
            self.previous_x_ = pose.x
            self.call_set_pen_service(255,0,0,3,0)
        elif pose.x <= 5.5 and self.previous_x_ > 5.5:
            self.previous_x_ = pose.x
            self.call_set_pen_service(0,255,0,3,0)    

    def call_set_pen_service(self,r,g,b,width,off):
        self.client = self.create_client(SetPen, "/turtle1/set_pen")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Waiting for the service...")

        req = SetPen.Request()
        req.r = r
        req.g = g
        req.b = b
        req.width = width
        req.off = off

        future = self.client.call_async(req)
        future.add_done_callback(partial(self.callback_set_pen))
        
    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("service call back failed %r", (e,))        


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()