from livox_frame_remap import livox_frame_remapping
import rclpy


def main(args=None):
    """Execute the subscriber to ensure we are listening on the topic"""
    rclpy.init(args=args)
    _livox_frame_remapping = livox_frame_remapping.LivoxFrameRemapping()
    rclpy.spin(_livox_frame_remapping)

    # close gracefully
    _livox_frame_remapping.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
