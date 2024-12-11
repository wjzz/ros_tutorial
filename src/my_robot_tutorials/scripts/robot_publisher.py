#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("my_robot_publisher")
    rospy.loginfo("Robot publisher started")
