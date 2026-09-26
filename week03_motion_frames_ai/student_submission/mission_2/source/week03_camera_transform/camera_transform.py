"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
import tf2_geometry_msgs
from geometry_msgs.msg import PointStamped


def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    """Return a hall_camera point expressed in base_link, or None if unavailable."""
    import tf2_geometry_msgs
    if point.header.frame_id != "hall_camera":
       raise ValueError("Point must be in hall_camera frame")
    try:
       transformed_point = tf_buffer.transform(point, "base_link")
       return transformed_point
    except Exception:
       return None
    
