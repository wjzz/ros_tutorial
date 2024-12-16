#!/usr/bin/env python3

"""Experiment to check how threading is done"""

import rospy

from std_msgs.msg import String

from rospy_tutorials.srv import AddTwoInts

import threading


def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo(f"Sum of {req.a} and {req.b} is {result}")
    rospy.loginfo(f"handler= {threading.get_ident()}")

    return result


def handle_add_two_ints2(req):
    result = req.a + req.b
    rospy.loginfo(f"Sum of {req.a} and {req.b} is {result}")
    rospy.loginfo(f"handler2= {threading.get_ident()}")

    return result


if __name__ == "__main__":
    rospy.init_node("led_status_server")
    rospy.loginfo("Led status server created")

    rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)
    rospy.Service("/add_two_ints2", AddTwoInts, handle_add_two_ints2)

    rospy.loginfo("Service has been started")

    rate = rospy.Rate(1)
    publisher = rospy.Publisher("/robot_test", String, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()

        msg = String()
        msg.data = "Hello"
        publisher.publish(msg)
        rospy.loginfo(f"main = {threading.get_ident()}")

    rospy.loginfo("Service has been shut down")
