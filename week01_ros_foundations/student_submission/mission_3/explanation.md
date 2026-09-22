# Mission 3

## Data To Command

The front_distance() record only valid measurements within the front sector of the robot. It returns the closest valid distance. Then, decide_velocity() uses the distance to decide whether the robot should move or stop. If there is no valid measurement or an obstacle is there, it returns 0.0. Otherwise the speed is 0.18 m/s.

## Missing Data Safety

The robot stops when there is no valid measurement because the system cannot confirm that the path is clear. Treating missing or invalid sensor data as clear could cause the robot to move toward the obstacle creating a error. Stopping is the  safer choice. 

## System Layers

The supplied ROS node receives lidar data from /scan and passes the reading to front_distance(). The result is passed to decide_velocity(), which produces a forward speed, and the ROS node publishes that proposed command on /student_cmd_vel. The command guard receives the proposed command and moves forwar if it is safe. It then publishes it on /cmd_vel. The result is used to move the robot. 
