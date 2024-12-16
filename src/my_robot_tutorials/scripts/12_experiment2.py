#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

import threading


def callback_receive_data(msg):
    rospy.loginfo("1: Message received")
    rospy.loginfo(msg)
    rospy.loginfo(f"handler= {threading.get_ident()}")


def callback_receive_data2(msg):
    rospy.loginfo("2: Message received")
    rospy.loginfo(msg)
    rospy.loginfo(f"handler= {threading.get_ident()}")
    while True:
        pass


if __name__ == "__main__":
    rospy.init_node("robot_subscriber")
    rospy.loginfo("Robot Subscriber started")

    rate = rospy.Rate(10)  # 10 Hz

    pub = rospy.Subscriber("/robot_news", String, callback_receive_data)
    pub = rospy.Subscriber("/robot_news2", String, callback_receive_data2)

    rospy.spin()

    rospy.loginfo("Robot Subscriber finished")
