#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Mynode(Node): # inherits from the node

    def __init__(self):
        super().__init__("mynode") # acessing all functionalities of the Node(node name) 
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback) # timer callback

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))
        

def main(args=None):
    rclpy.init(args=args) #initializing ros2 communications
    node = Mynode()
    rclpy.spin(node) #for continously running the node and callbacks
    rclpy.shutdown()

if __name__ == '__main__': #which will execute in terimnal also
    main()