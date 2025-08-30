#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test") # Initialize the node with the name "py_test"
        self.counter_ = 0
        self.get_logger().info("Hello ROS2") # Log a message
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Hello {self.counter_}")

def main(args=None):
    rclpy.init(args=args) # Initialize the ROS2 Python client library
    # node = Node("py_test") # Create a new node
    node = MyNode() # Create an instance of MyNode
    rclpy.spin(node) # Keep the node alive to listen for messages
    rclpy.shutdown()

if __name__ == "__main__":
    main()