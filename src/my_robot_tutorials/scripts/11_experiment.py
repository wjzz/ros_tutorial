#!/usr/bin/env python3

"""Experiment to check how threading is done"""

import rospy

from std_msgs.msg import String

from rospy_tutorials.srv import AddTwoInts


def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo(f"Sum of {req.a} and {req.b} is {result}")
    return result


def handle_call(req):
    return "OK"


if __name__ == "__main__":
    rospy.init_node("led_status_server")
    rospy.loginfo("Led status server created")

    rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)

    rospy.loginfo("Service has been started")

    rate = rospy.Rate(1)
    publisher = rospy.Publisher("/robot_test", String, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()

        msg = String()
        msg.data = "Hello"
        publisher.publish(msg)

    rospy.loginfo("Service has been shut down")
