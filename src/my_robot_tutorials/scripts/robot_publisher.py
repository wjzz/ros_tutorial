#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

from dataclasses import dataclass


@dataclass(frozen=True)
class Robot:
    id: int
    velocity: int


def random_robot() -> Robot:
    import random

    ids = [1, 2, 3]

    id = random.choice(ids)
    velocity = random.randint(-10, 10)

    return Robot(id, velocity)


class Publisher:
    def __init__(self):
        self.pub = rospy.Publisher("/robot_news", String, queue_size=10)

    def publish_message(self, robot: Robot):
        import json

        msg = String()
        msg.data = json.dumps(robot.__dict__)
        self.pub.publish(msg)


if __name__ == "__main__":
    rospy.init_node(
        "my_robot_publisher", anonymous=True
    )  # anonymous makes it possible to run the same node multiple time
    rospy.loginfo("Robot publisher started")

    rate = rospy.Rate(10)
    publisher = Publisher()

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()

        robot = random_robot()
        publisher.publish_message(robot)

    rospy.loginfo("Robot publisher stopped")
