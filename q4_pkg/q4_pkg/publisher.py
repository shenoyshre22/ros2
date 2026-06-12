#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class TempPublisher(Node):
    def __init__(self):
        super().__init__('temp_pub_node')
        self.pub = self.create_publisher(Int32, 'temperature_stream', 10)
        self.create_timer(1.5, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(5, 45)  # Range covering cold, normal, hot
        self.pub.publish(msg)
        self.get_logger().info(f"Current Temperature Reading: {msg.data}°C")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TempPublisher())
    rclpy.shutdown()