#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

import threading
import time
import os


def callback_receive_data(msg):
    rospy.loginfo(f"handler= {threading.get_ident()}")
    while True:
        pass


if __name__ == "__main__":
    rospy.init_node("robot_subscriber")
    rospy.loginfo("Robot Subscriber started")

    print(os.getpid())

    rate = rospy.Rate(10)  # 10 Hz

    pub = rospy.Subscriber("/robot_news", String, callback_receive_data)

    while True:
        rospy.loginfo("=== Printing ===")
        for thread in threading.enumerate():
            rospy.loginfo(thread.name)
        time.sleep(1)
