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
