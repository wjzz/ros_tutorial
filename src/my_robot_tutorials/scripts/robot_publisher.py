#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


class Publisher:
    def __init__(self):
        self.pub = rospy.Publisher("/robot_news", String, queue_size=10)

    def publish_message(self):
        msg = String()
        msg.data = "Hello"
        self.pub.publish(msg)


if __name__ == "__main__":
    rospy.init_node("my_robot_publisher")
    rospy.loginfo("Robot publisher started")

    rate = rospy.Rate(10)
    publisher = Publisher()

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()
        publisher.publish_message()

    rospy.loginfo("Robot publisher stopped")
