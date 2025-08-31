#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        
        self.start_number = 0
        self.publisher_ = self.create_publisher(Int64, "number_topic", 10)
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info("Number Publisher Node has been started")
        
    def timer_callback(self):
        msg = Int64()
        msg.data = f"This is the start number: {self.start_number}"
        self.publisher_.publish(msg)
        self.start_number += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()