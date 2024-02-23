from rclpy.node import Node
from std_msgs.msg import String
import std_msgs.msg as std_msgs
import sensor_msgs.msg as sensor_msgs

class LivoxFrameRemapping(Node):
    def __init__(self):
        super().__init__("livox_frame_remapping")
        self.subscriber_left = self.create_subscription(
            sensor_msgs.PointCloud2,    # Msg type
            'livox/lidar_192_168_1_109',# topic
            self.listener_callback1,     # Function to call
            10                          # QoS
        )
        self.subscriber_right = self.create_subscription(
            sensor_msgs.PointCloud2,    # Msg type
            'livox/lidar_192_168_1_113',# topic
            self.listener_callback2,     # Function to call
            10                          # QoS
        )
        self.publisher_left = self.create_publisher(sensor_msgs.PointCloud2, 'livox/lidar_192_168_1_110', 10)
        self.publisher_right = self.create_publisher(sensor_msgs.PointCloud2, 'livox/lidar_192_168_1_114', 10)

    def listener_callback1(self, msg):
        header1 = std_msgs.Header(frame_id="lidar_left_link")
        self.publisher_left.publish(
            sensor_msgs.PointCloud2(
                header=header1,
                height=msg.height,
                width=msg.width,
                fields=msg.fields,
                is_bigendian=msg.is_bigendian,
                point_step=msg.point_step,
                row_step=msg.row_step,
                data=msg.data,
                is_dense=msg.is_dense
            )
        )
    def listener_callback2(self, msg):
        header1 = std_msgs.Header(frame_id="lidar_right_link")
        self.publisher_right.publish(
            sensor_msgs.PointCloud2(
                header=header1,
                height=msg.height,
                width=msg.width,
                fields=msg.fields,
                is_bigendian=msg.is_bigendian,
                point_step=msg.point_step,
                row_step=msg.row_step,
                data=msg.data,
                is_dense=msg.is_dense
            )
        )