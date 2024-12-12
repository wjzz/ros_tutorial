#!/usr/bin/env python3

import rospy
from my_robot_msgs.srv import SetLed

import time


def call_service(led_number: int, bit: bool):
    try:
        rospy.loginfo(f"Calling the service with bit = {bit}")
        client = rospy.ServiceProxy("/set_led", SetLed)
        response = client(led_number, bit)
        rospy.loginfo(f"Got response = {response.response}")
    except rospy.ServiceException as e:
        rospy.logwarn(f"Service failed {e}")


if __name__ == "__main__":
    rospy.init_node("set_led_client")

    rospy.wait_for_service("/set_led")

    while True:
        # battery is charged
        call_service(led_number=2, bit=True)
        time.sleep(7.0)

        # batter is empty
        call_service(led_number=2, bit=False)
        time.sleep(3.0)
