#!/usr/bin/env python3

import rospy
from my_robot_msgs.srv import ComputeDiskArea

if __name__ == "__main__":
    rospy.init_node("compute_area_client")

    rospy.wait_for_service("/compute_area")

    try:
        rospy.loginfo("Calling the service")
        client = rospy.ServiceProxy("/compute_area", ComputeDiskArea)
        response = client(1.0)
        rospy.loginfo(f"Got result = {response.area}")
    except rospy.ServiceException as e:
        rospy.logwarn(f"Service failed {e}")
