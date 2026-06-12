#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class PublisherOne(Node):
    def __init__(self):
        super().__init__('pub_one_node')
        self.pub = self.create_publisher(Int32, 'num_one', 10)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(0, 5)
        self.pub.publish(msg)
        self.get_logger().info(f"Published to num_one: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(PublisherOne())
    rclpy.shutdown()