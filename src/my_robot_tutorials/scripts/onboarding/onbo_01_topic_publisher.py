#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

import random

if __name__ == "__main__":
    rospy.init_node("example_topic_publisher")
    rospy.loginfo("Node has been started")

    rate = rospy.Rate(10)  # 10 Hz

    publisher = rospy.Publisher("/onboarding", Int64, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Sending message")
        rate.sleep()

        msg = Int64()
        msg.data = random.randint(0, 10)
        publisher.publish(msg)

    rospy.loginfo("Node was stopped")
