#!/usr/bin/env python3

import rospy

from my_robot_msgs.srv import SetLed
import math


class Leds:
    def __init__(self):
        self.leds = [False, False, False]

    def set_bit(self, led_number: int, bit: bool):
        self.leds[led_number] = bit

    def print_all(self):
        print(self.leds)


leds = Leds()


def handle_set_led(req):
    led_number = req.led_number
    bit = req.bit

    if led_number not in [0, 1, 2]:
        return f"Error: wrong led number {led_number}"

    rospy.loginfo("I will set led#{led_number} to {bit}")

    leds.set_bit(led_number, bit)

    rospy.loginfo(f"Current state: {leds.print_all()}")

    return "OK"


if __name__ == "__main__":
    rospy.init_node("led_status_server")
    rospy.loginfo("Led status server created")

    rospy.Service("/set_led", SetLed, handle_set_led)

    rospy.loginfo("Service has been started")

    rospy.spin()

    rospy.loginfo("Service has been shut down")
