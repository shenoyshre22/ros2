#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TempClassifier(Node):
    def __init__(self):
        super().__init__('temp_sub_node')
        self.sub = self.create_subscription(Int32, 'temperature_stream', self.callback, 10)

    def callback(self, msg):
        temp = msg.data
        if temp < 15:
            status = "Cold (<15°C)"
        elif 15 <= temp <= 30:
            status = "Normal (15-30°C)"
        else:
            status = "Hot (>30°C)"
        self.get_logger().info(f" Analysis -> Reading: {temp}°C | Metric: {status}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TempClassifier())
    rclpy.shutdown()