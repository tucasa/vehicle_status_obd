#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import obd
import rclpy
from rclpy.node import Node
from rclpy.time import Time
from geometry_msgs.msg import TwistStamped


class PublishVehicleVelocity(Node):
    def __init__(self):
        super().__init__('publish_twist')
        self.declare_parameter('port', '/dev/ttyUSB0')
        port = self.get_parameter('port').get_parameter_value().string_value
        self.publisher = self.create_publisher(TwistStamped, 'can_twist', 10)
        self.connection = obd.Async(portstr=port, delay_cmds=0)
        self.connection.watch(obd.commands.SPEED, callback=self.new_speed)
        self.connection.start()

    def new_speed(self, r):
        vel = TwistStamped()
        vel.header.frame_id = '/vehicle'
        now = self.get_clock().now().to_msg() if getattr(r, 'time', None) is None else Time(seconds=r.time).to_msg()
        vel.header.stamp = now
        vel.twist.linear.x = r.value.magnitude if getattr(r, 'value', None) is not None else 0.0
        self.publisher.publish(vel)


def main():
    rclpy.init()
    node = PublishVehicleVelocity()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.connection.close()
        node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() 