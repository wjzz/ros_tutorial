#!/usr/bin/env python3

import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == "__main__":
    rospy.init_node("add two ints client")

    rospy.wait_for_service("/add_two_ints")

    try:
        rospy.loginfo("Calling the service")
        client = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        response = client(2, 6)
        rospy.loginfo(f"Got result = {response.sum}")
    except rospy.ServiceException as e:
        rospy.logwarn(f"Service failed {e}")
