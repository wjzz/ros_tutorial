#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

from collections import defaultdict
from pprint import pprint

frequencies = defaultdict(int)


def callback_receive_data(msg):
    rospy.loginfo("Message received")
    rospy.loginfo(msg)

    frequencies[msg.data] += 1

    rospy.loginfo(f"{pprint(frequencies)}")


if __name__ == "__main__":
    rospy.init_node("example_topic_subscriber")
    rospy.loginfo("Topic Subscriber started")

    pub = rospy.Subscriber("/onboarding", Int64, callback_receive_data)

    rospy.spin()

    rospy.loginfo("Topic Subscriber finished")
