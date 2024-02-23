from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="laser_filters",
            executable="scan_to_scan_filter_chain",
            remappings=[
                ("scan", "/livox/lidar_scan_left"),
                ("scan_filtered", "/livox/lidar_scan_left_filtered")
            ],
            parameters=[
                PathJoinSubstitution([
                    get_package_share_directory("laser_filters"),
                    "examples", "angular_filter_example.yaml",
                ])],
        )
        Node(
            package="laser_filters",
            executable="scan_to_scan_filter_chain",
            remappings=[
                ("scan", "/livox/lidar_scan_right"),
                ("scan_filtered", "/livox/lidar_scan_right_filtered")
            ],
            parameters=[
                PathJoinSubstitution([
                    get_package_share_directory("laser_filters"),
                    "examples", "angular_filter_example.yaml",
                ])],
        )
    ])
