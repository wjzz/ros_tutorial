#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>

bool handle_add_two_ints(rospy_tutorials::AddTwoInts::Request &req, rospy_tutorials::AddTwoInts::Response &resp)
{
    int result = req.a + req.b;
    ROS_INFO("%d + %d = %d", (int)req.a, (int)req.b, result);

    resp.sum = result;

    // The service call was successful
    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "add_two_inits_server");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("/add_two_ints", handle_add_two_ints);

    ros::spin();
}