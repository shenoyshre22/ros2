#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SubscriberY(Node):
    def __init__(self):
        super().__init__('sub_y_node')
        self.sub = self.create_subscription(Int32, 'topic_z', self.callback, 10)

    def callback(self, msg):
        # Process forward only if number is even
        if msg.data % 2 == 0:
            self.get_logger().warn(f"🏁 Y Final Output (Multiple of 3 and Even): {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(SubscriberY())
    rclpy.shutdown()