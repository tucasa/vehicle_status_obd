#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import obd
import rospy
from geometry_msgs.msg import TwistStamped


class PublishVehicleVelocity:
    def __init__(self):
        rospy.init_node('publish_twist')

        self.pub = rospy.Publisher('/can_twist', TwistStamped, queue_size=10)

        connection = obd.Async(portstr='/dev/ttyUSB0', delay_cmds=0)

        connection.watch(obd.commands.SPEED, self.new_speed)
        connection.start()

        rospy.spin()

        connection.close()

    def new_speed(self, r):
        vel = TwistStamped()
        vel.header.frame_id = '/vehicle'
        vel.header.stamp = rospy.Time.from_sec(r.time)
        vel.twist.linear.x = r.value.magnitude
        
        self.pub.publish(vel)


def main():
    try:
        PublishVehicleVelocity()
    except rospy.ROSInterruptException:
        pass



if __name__ == '__main__':
    main()
