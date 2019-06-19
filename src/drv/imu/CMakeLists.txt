cmake_minimum_required(VERSION 2.8.3)
project(imu)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED

    roscpp
    diagnostics
    sensor_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

###################################
## catkin specific configuration ##
###################################
catkin_package(

    CATKIN_DEPENDS roscpp
)

###########
## Build ##
###########
include_directories(

    include
    ${catkin_INCLUDE_DIRS}
)

add_library(${PROJECT_NAME}

    src/imu_driver.cpp
)

add_executable(${PROJECT_NAME}_node 

    node/imu_node.cpp
)

target_link_libraries(${PROJECT_NAME}_node

    ${catkin_LIBRARIES}
    ${PROJECT_NAME}
)

#############
## Install ##
#############

#############
## Testing ##
#############
