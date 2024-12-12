#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "add_two_inits_client");
    ros::NodeHandle nh;
    ROS_INFO("Client initialized");

    ros::ServiceClient client = nh.serviceClient<rospy_tutorials::AddTwoInts>("/add_two_ints");

    rospy_tutorials::AddTwoInts srv;
    srv.request.a = 123;
    srv.request.b = 100;

    ROS_INFO("Sending request");
    if (client.call(srv))
    {
        // process data
        ROS_INFO("Returned sum is %d", (int)srv.response.sum);
    }
    else
    {
        // service failed
        ROS_WARN("Service call failed");
    }
}