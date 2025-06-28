#!/usr/bin/env python3
import rclpy
from rclpy.lifecycle import  LifecycleNode, LifecycleState, TransitionCallbackReturn
from example_interfaces.msg import Int64

class Mynode(LifecycleNode):

    def __init__(self):
        super().__init__("lifecyclenode")
        self.get_logger().info("IN on_constructor")
        self.pub_ = None
        self.timer_ = None

    def on_configure(self, state: LifecycleState):
        self.get_logger().info("IN on_configure")
        self.pub_ = self.create_lifecycle_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1.0, self.publish_number)
        self.timer_.cancel()
        return TransitionCallbackReturn.SUCCESS
    
    def on_cleanup(self, state: LifecycleState):
        self.get_logger().info("IN on_cleanup")
        self.destroy_lifecycle_publisher(self.pub_)
        self.destroy_timer(self.timer_)
        return TransitionCallbackReturn.SUCCESS
    
    def on_activate(self, state: LifecycleState):
        self.get_logger().info("IN on_activate")
        self.timer_.reset()
        return super().on_activate(state)
    
    def on_deactivate(self, state: LifecycleState):
        self.get_logger().info("IN on_deactivate")
        self.timer_.cancel()
        return super().on_deactivate(state)  # which will going to activate all the lifecycle publishers
    
    def on_shutdown(self, state: LifecycleState):
        self.get_logger().info("IN on_shutdown")
        self.destroy_lifecycle_publisher(self.pub_)
        self.destroy_timer(self.timer_)
        return TransitionCallbackReturn.SUCCESS

    def publish_number(self):
        msg = Int64()
        msg.data = 5
        self.get_logger().info("Publishing number")
        self.pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()