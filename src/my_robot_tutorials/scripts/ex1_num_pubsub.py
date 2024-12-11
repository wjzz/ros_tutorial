#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64


class Publisher:
    def __init__(self):
        self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)

    def publish_message(self, number: int):
        msg = Int64()
        msg.data = number
        self.pub.publish(msg)


class Counter:
    def __init__(self):
        self.total = 0
        self.pub = Publisher()

    def add_data_point(self, number: int):
        self.total += number

    def publish_total(self):
        self.pub.publish_message(self.total)


counter = Counter()


def callback_receive_data(msg):
    rospy.loginfo("Message received")
    rospy.loginfo(msg)

    number = msg.data

    counter.add_data_point(number)
    counter.display_all()


if __name__ == "__main__":
    rospy.init_node(
        "number_pubsub", anonymous=True
    )  # anonymous makes it possible to run the same node multiple time
    rospy.loginfo("Number publisher started")

    pub = rospy.Subscriber("/number", Int64, callback_receive_data)

    rospy.spin()

    rospy.loginfo("Number pubsub stopped")
