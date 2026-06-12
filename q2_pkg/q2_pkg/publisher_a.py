#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PublisherA(Node):
    def __init__(self):
        super().__init__('pub_a_node')
        self.pub = self.create_publisher(Int32, 'topic_a', 10)
        self.count = 1
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count
        self.pub.publish(msg)
        self.get_logger().info(f"Incrementing: {msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(PublisherA())
    rclpy.shutdown()