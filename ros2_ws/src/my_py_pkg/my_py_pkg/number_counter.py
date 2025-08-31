#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class CounterNumberNode(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.count = 0
        self.subscriber_ = self.create_subscription(
            Int64,
            "number_topic",
            self.listener_callback,
            10
        )
    
    def listener_callback(self, msg):
        self.get_logger().info(f"Received number: {msg.data}")
        self.count += 1
        self.get_logger().info(f"Sum: {self.count}")


def main(args=None):
    rclpy.init(args=args)
    node = CounterNumberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
