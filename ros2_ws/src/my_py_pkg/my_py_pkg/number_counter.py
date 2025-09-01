#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class CounterNumberNode(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.counter_ = 0
        self.subscriber_ = self.create_subscription(
            Int64,
            "number",
            self.listener_callback,
            10
        )
        
        self.publisher_ = self.create_publisher(
            Int64,
            "number_count",
            10
        )
        self.server_ = self.create_service(SetBool, "reset_counter", self.callback_reset_counter)
        self.timer_ = self.create_timer(0.5, self.publish_number_count)
        self.get_logger().info("Number Counter Node has been started")
        
    def listener_callback(self, msg):
        self.counter_ += msg.data
        self.get_logger().info(f"Received: {msg.data}, Total Count: {self.counter_}")
    
    def publish_number_count(self):
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)
    
    def callback_reset_counter(self, request, response):
        if request.data:
            self.counter_ = 0
            response.success = True
            response.message = "Counter has been reset to zero."
        else:
            response.success = False
            response.message = "Counter reset failed."
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CounterNumberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
