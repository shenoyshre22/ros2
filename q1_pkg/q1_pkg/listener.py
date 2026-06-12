#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Q1Listener(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.val1, self.val2 = -1, -2  # Set non-matching baselines
        self.sub1 = self.create_subscription(Int32, 'num_one', self.cb1, 10)
        self.sub2 = self.create_subscription(Int32, 'num_two', self.cb2, 10)
        self.match_pub = self.create_publisher(Int32, 'matching_output', 10)

    def cb1(self, msg):
        self.val1 = msg.data
        self.check_logic()

    def cb2(self, msg):
        self.val2 = msg.data
        self.check_logic()

    def check_logic(self):
        if self.val1 == self.val2:
            match_msg = Int32()
            match_msg.data = self.val1
            self.match_pub.publish(match_msg)
            self.get_logger().warn(f" MATCH DETECTED AND PUBLISHED: {self.val1}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(Q1Listener())
    rclpy.shutdown()