#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TimestampSubscriber(Node):
    def __init__(self):
        super().__init__('timestamp_sub_node')
        self.sub = self.create_subscription(String, 'text_topic', self.callback, 10)

    def callback(self, msg):
        # Extract native ROS clock time parameters
        now = self.get_clock().now()
        seconds = now.seconds_nanoseconds()[0]
        self.get_logger().info(f" [Timestamp: {seconds}s] Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TimestampSubscriber())
    rclpy.shutdown()