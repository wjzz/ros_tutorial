#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "publisher", ros::init_options::AnonymousNode);
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);

    ROS_INFO("Node has been started");

    ros::Rate rate(10);

    while (ros::ok())
    {
        ROS_INFO("Hello");
        std_msgs::String msg;
        msg.data = "HI!!!";
        pub.publish(msg);
        rate.sleep();
    }
}
