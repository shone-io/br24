FROM shoneio/ros:kinetic-workspace-core

RUN sudo apt-get update && sudo apt-get install -y \
    curl \
    python-tk

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN sudo python get-pip.py

RUN sudo -H pip install pillow

COPY ./shone_ros_msgs src/shone_ros_msgs/.
COPY ./br24 src/br24/.
RUN catkin build

ENV ROS_HOSTNAME=br24
ENV ROS_MASTER_URI=http://master:11311
