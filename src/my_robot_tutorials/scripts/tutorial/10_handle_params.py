#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

import random


class Publisher:
    def __init__(self):
        self.pub = rospy.Publisher("/number", Int64, queue_size=10)

    def publish_message(self, number: int):
        import json

        msg = Int64()
        msg.data = number
        self.pub.publish(msg)


if __name__ == "__main__":
    rospy.init_node(
        "number_publisher", anonymous=True
    )  # anonymous makes it possible to run the same node multiple time
    rospy.loginfo("Number publisher started")

    # this is new
    publish_frequency = rospy.get_param("/number_publish_frequency")
    rate = rospy.Rate(publish_frequency)

    publisher = Publisher()

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()

        number = random.randint(0, 10)
        publisher.publish_message(number)

    rospy.loginfo("Number publisher stopped")
