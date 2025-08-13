#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import obd
import rospy
from geometry_msgs.msg import TwistStamped


class PublishVehicleVelocity:
    def __init__(self):
        rospy.init_node('publish_twist')

        self.pub = rospy.Publisher('/can_twist', TwistStamped, queue_size=10)

        self.connection = obd.OBD(portstr='/dev/ttyUSB0')

    def publish_can_twist(self):
        r = rospy.Rate(80)
        while not rospy.is_shutdown():
            res = self.connection.query(obd.commands.SPEED)
            vel = TwistStamped()
            vel.header.frame_id = '/vehicle'
            vel.header.stamp = rospy.Time.from_sec(res.time)
            vel.twist.linear.x = res.value.magnitude
            self.pub.publish(vel)
            r.sleep()


def main():
    try:
        pub_twist = PublishVehicleVelocity()
        pub_twist.publish_can_twist()
    except rospy.ROSInterruptException:
        pub_twist.connection.close()


if __name__ == '__main__':
    main()
