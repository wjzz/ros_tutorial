#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Robot:
    id: int
    velocity: int


class RobotData:
    def __init__(self):
        self.robots = {}

    def add_data_point(self, robot: Robot):
        self.robots[robot.id] = robot.velocity

    def display_all(self):
        for id, velocity in sorted(self.robots.items()):
            print(f"Robot[{id}] = {velocity}")


robotData = RobotData()


def callback_receive_data(msg):
    rospy.loginfo("Message received")
    rospy.loginfo(msg)

    dictionary = json.loads(msg.data)
    robot = Robot(dictionary["id"], dictionary["velocity"])

    robotData.add_data_point(robot)
    robotData.display_all()


if __name__ == "__main__":
    rospy.init_node("robot_subscriber")
    rospy.loginfo("Robot Subscriber started")

    rate = rospy.Rate(10)  # 10 Hz

    pub = rospy.Subscriber("/robot_news", String, callback_receive_data)

    rospy.spin()

    rospy.loginfo("Robot Subscriber finished")
