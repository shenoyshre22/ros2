#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SubscriberZ(Node):
    def __init__(self):
        super().__init__('sub_z_node')
        self.sub = self.create_subscription(Int32, 'topic_a', self.callback, 10)
        self.pub = self.create_publisher(Int32, 'topic_z', 10)

    def callback(self, msg):
        # Pass forward only if multiple of 3
        if msg.data % 3 == 0:
            self.pub.publish(msg)
            self.get_logger().info(f"Z Filter Passed (Multiple of 3): {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(SubscriberZ())
    rclpy.shutdown()