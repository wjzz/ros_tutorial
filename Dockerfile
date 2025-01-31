FROM ros:noetic-ros-core

RUN apt update && apt install -y build-essential ros-noetic-rospy-tutorials

WORKDIR /home/root

COPY . .

SHELL ["/bin/bash", "-o", "pipefail","-c"]

WORKDIR /home/root

RUN echo "source /opt/ros/noetic/setup.bash" >>/home/root/.bash_profile
RUN source /opt/ros/noetic/setup.bash && catkin_make
RUN echo "source devel/setup.sh" >>/home/root/.bash_profile
