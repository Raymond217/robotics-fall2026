# Mission 2

## Frame Context

The rear camera is attached to the robot, so its position relative to `base_link` stays the same even when the robot moves. The hallway camera is fixed in the environment, while the robot moves, so its position relative to `base_link` changes as the robot moves. The `odom` frame connects the moving robot to the fixed hallway camera.


## Improved Changes

The improved prompt clearly specifies that the source frame is `hall_camera` and that the target frame is `base_link`. It also requires the point's original timestamp to be preserved so that TF can use the transform corresponding to when the camera observation was made.

Instead of using the hard-coded position offsets, the program uses the given TF buffer to calculate the correct transformation. If the transform is not available, the function returns `None` instead of guessing a position. The program also should not be able publish any movement commands, so transforming the camera point cannot accidentally move the robot.


## Initial Analysis

The initial AI response assumes that the source frame is hall_camera and the target frame is base_link, but it does not clearly verify that these are the correct frames. It creates a PointStamped and sets the frame ID, but it uses the current time instead of necessarily preserving the timestamp of when the camera observation was made.

The response does use a TF buffer and listener, which is good, but it does not explain what happens if the required transform is not available at the observation timestamp. It catches an exception and returns None, but the behavior could be more specific.

The example does not use hard-coded position offsets, which is good. However, it assumes that the TF tree will provide the required transform. It also does not put any robot motion commands, so it does not directly control the robot. A better implementation should explicitly require the original point timestamp, use the supplied TF buffer, reject points from the wrong source frame, and safely return None when the transform is unavailable.

## Initial Output

To convert a point detected by the hallway camera into the robot's `base_link` frame, you can use ROS 2's `tf2` library. The basic idea is to create a `PointStamped` message containing the point in the hallway camera's frame, then use a `tf2_ros.Buffer` to look up the transform from the camera frame to `base_link`.

Here is an example:

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
import tf2_geometry_msgs

class PointTransformer(Node):
def **init**(self):
super().**init**('point_transformer')

```
    self.tf_buffer = tf2_ros.Buffer()
    self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

def transform_point(self, x, y, z):
    point = PointStamped()
    point.header.frame_id = 'hall_camera'
    point.header.stamp = self.get_clock().now().to_msg()

    point.point.x = x
    point.point.y = y
    point.point.z = z

    try:
        transformed_point = self.tf_buffer.transform(
            point,
            'base_link'
        )

        self.get_logger().info(
            f'Transformed point: x={transformed_point.point.x}, '
            f'y={transformed_point.point.y}, '
            f'z={transformed_point.point.z}'
        )

        return transformed_point

    except Exception as e:
        self.get_logger().error(f'Could not transform point: {e}')
        return None
```

def main(args=None):
rclpy.init(args=args)

```
node = PointTransformer()

# Example point detected by the hallway camera
node.transform_point(1.0, 0.5, 2.0)

rclpy.spin_once(node, timeout_sec=1.0)

node.destroy_node()
rclpy.shutdown()
```

if **name** == '**main**':
main()


## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
import tf2_geometry_msgs

class PointTransformer(Node):
def **init**(self):
super().**init**('point_transformer')

```
    self.tf_buffer = tf2_ros.Buffer()
    self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

def transform_point(self, x, y, z):
    point = PointStamped()
    point.header.frame_id = 'hall_camera'
    point.header.stamp = self.get_clock().now().to_msg()

    point.point.x = x
    point.point.y = y
    point.point.z = z

    try:
        transformed_point = self.tf_buffer.transform(
            point,
            'base_link'
        )

        self.get_logger().info(
            f'Transformed point: x={transformed_point.point.x}, '
            f'y={transformed_point.point.y}, '
            f'z={transformed_point.point.z}'
        )

        return transformed_point

    except Exception as e:
        self.get_logger().error(f'Could not transform point: {e}')
        return None
```

def main(args=None):
rclpy.init(args=args)

```
node = PointTransformer()

# Example point detected by the hallway camera
node.transform_point(1.0, 0.5, 2.0)

rclpy.spin_once(node, timeout_sec=1.0)

node.destroy_node()
rclpy.shutdown()
```

if **name** == '**main**':
main()


## Live Issue

There is no error.

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-25T21:04:01.467157+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'source': 'reference', 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}}}

## Synthesis

The initial AI response assumed the source was `hall_camera` and the target was `base_link`, but it did not handle the observation timestamp well or explain what should happen when the transform is not available. The improved prompt requires the correct source and target frames, the use of the TF buffer, the preservation of the timestamp, and no hard-coded offsets.

Using the wrong transform could make the robot calculate the wrong position of a person or object. This could cause the robot to get too close to someone or move in an unsafe direction. The course tests for the correct transformed coordinates and unavailable-transform behavior, which helps detect this problem.

If transform data is not available, the robot should not guess the object's location or move based on the invalid data. It should return `None` and wait until valid transform information is available.

