#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

# this is the function launch  system will look for
def generate_launch_description():

    livox_frame_remapping_publisher = Node(
        package='livox_frame_remap',
        executable='livox_frame_remap_node',
        output='screen',
    )
    
    # create and return launch description object
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [get_package_share_directory('deliverybot_description'), 
                    '/launch/launch_deliverybot.launch.py']),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [get_package_share_directory('livox_ros_driver2'), 
                    '/launch_ROS2/rviz_MID360_launch.py']),
            ),
            livox_frame_remapping_publisher,
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [get_package_share_directory('pointcloud_to_laserscan'), 
                    '/launch/livox_pointcloud_to_laserscan_launch.py']),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [get_package_share_directory('realsense2_camera'), 
                    '/launch/rs_launch.py']),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [get_package_share_directory('depthimage_to_laserscan'), 
                    '/launch/depthimage_to_laserscan-launch.py']),
            ),
        ]
    )