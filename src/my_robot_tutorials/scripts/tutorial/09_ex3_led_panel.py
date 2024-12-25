#!/usr/bin/env python3

import rospy

from my_robot_msgs.srv import SetLed
from my_robot_msgs.msg import LedStatus


class Leds:
    def __init__(self):
        self.leds = [False, False, False]

    def set_bit(self, led_number: int, bit: bool):
        self.leds[led_number] = bit

    def print_all(self):
        print(self.leds)

    def to_led_status(self) -> LedStatus:
        result = LedStatus()
        result.led1 = self.leds[0]
        result.led2 = self.leds[1]
        result.led3 = self.leds[2]
        return result


leds = Leds()


def handle_set_led(req):
    led_number = req.led_number
    bit = req.bit

    if led_number not in [0, 1, 2]:
        return f"Error: wrong led number {led_number}"

    rospy.loginfo(f"I will set led#{led_number} to {bit}")

    leds.set_bit(led_number, bit)

    rospy.loginfo("Current state:")
    leds.print_all()

    return "OK"


if __name__ == "__main__":
    rospy.init_node("led_status_server")
    rospy.loginfo("Led status server created")

    rospy.Service("/set_led", SetLed, handle_set_led)

    rospy.loginfo("Service has been started")

    rate = rospy.Rate(1)
    publisher = rospy.Publisher("/led_Status", LedStatus, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Preparing a message")
        rate.sleep()

        publisher.publish(leds.to_led_status())

    rospy.loginfo("Service has been shut down")
