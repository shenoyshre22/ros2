#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TextPublisher(Node):
    def __init__(self):
        super().__init__('text_pub_node')
        self.pub = self.create_publisher(String, 'text_topic', 10)
        self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Standard Operating Metric Status: OK"
        self.pub.publish(msg)
        self.get_logger().info("Dispatched data stream packet.")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TextPublisher())
    rclpy.shutdown()