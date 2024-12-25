#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('my_first_python_publisher')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10) # 10 Hz

    pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)
    count = 1

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()

        msg = String()
        msg.data = f"Example message #{count}"
        pub.publish(msg)
        count += 1

    rospy.loginfo("Node was stopped")
