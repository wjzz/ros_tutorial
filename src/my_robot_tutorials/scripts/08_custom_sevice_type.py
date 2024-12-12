#!/usr/bin/env python3

import rospy

from my_robot_msgs.srv import ComputeDiskArea
import math


def handle_compute_area(req):
    result = req.radius * req.radius * math.pi
    rospy.loginfo(f"Area of a disk of radius {req.radius} is {result}")
    return result


if __name__ == "__main__":
    rospy.init_node("compute_area_server")
    rospy.loginfo("Compute area server created")

    rospy.Service("/compute_area", ComputeDiskArea, handle_compute_area)

    rospy.loginfo("Service has been started")

    rospy.spin()

    rospy.loginfo("Service has been shut down")
