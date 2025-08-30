#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) # Initialize the ROS2 Python client library
    node = Node("py_test") # Create a new node
    node.get_logger().info("Hello ROS2") # Log a message
    rclpy.spin(node) # Keep the node alive to listen for messages
    rclpy.shutdown()

if __name__ == "__main__":
    main()