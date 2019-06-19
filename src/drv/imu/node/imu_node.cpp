// ROS
#include <ros/ros.h>

// Driver
#include "imu_driver.h"

int main(int argc, char **argv) {
  ros::init(argc, argv, "imu_node");
  ros::NodeHandle nh;

  diagnostic_updater::Updater updater;
  updater.setHardwareID("imu");

  ImuDriver id;
  id.init(nh, updater);

  ros::spin();

  return 0;
}