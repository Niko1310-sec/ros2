#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
import random
from turtlesim.msg import Pose

class Teleopclient(Node):

    def __init__(self):
        super().__init__("teleop_client_node")
        #creating a client
        self.client = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute")
        #wait for the service
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for the service updated")

        self.pose_sub = self.create_subscription(Pose, "/turtle1/pose",self.pose_callback, 10)   # pose subscriber

        self.timer = self.create_timer(2.0, self.teleport_turtle)
        self.get_logger().info('Teleport client node has started')

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f"Turtle Position: x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f} ")    # defining the pose 

    def teleport_turtle(self): #client request
        req = TeleportAbsolute.Request()
        req.x = random.uniform(1.0, 6.0)
        req.y = random.uniform(1.0, 6.0)
        req.theta = 0.0
        self.get_logger().info(f"Teleporting turtle to x={req.x} y={req.y} theta={req.theta}")

        self.future = self.client.call_async(req)
        self.future.add_done_callback(self.teleport_callback)   # this function automatically called when service responds

    def teleport_callback(self, future): 
        try:
            self.response = future.result()
            self.get_logger().info("the turtle is teleported to")
        except Exception as e:
            self.get_logger().error("the teleport service is failed", (e))         
          
def main(args=None):
    rclpy.init(args=args)
    node = Teleopclient()
    rclpy.spin(node)
    rclpy.shutdown()
