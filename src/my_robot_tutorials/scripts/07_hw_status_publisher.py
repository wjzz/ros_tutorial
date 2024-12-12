#!/usr/bin/env python3

import rospy
from my_robot_msgs.msg import HardwareStatus

if __name__ == "__main__":
    rospy.init_node("hardware publisher")
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10)  # 10 Hz

    pub = rospy.Publisher("/hardware_status", HardwareStatus, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing message")
        rate.sleep()

        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_up = True
        msg.debug_message = "Everything OK"
        pub.publish(msg)

    rospy.loginfo("Node was stopped")
