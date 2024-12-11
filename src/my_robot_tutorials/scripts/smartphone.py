#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_receive_data(msg):
    rospy.loginfo("Message received")
    rospy.loginfo(msg)

if __name__ == "__main__":
    rospy.init_node('my_first_python_subscriber')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10) # 10 Hz

    pub = rospy.Subscriber("/robot_news_radio", String, callback_receive_data)

    rospy.spin()