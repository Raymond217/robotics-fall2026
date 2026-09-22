# Mission 1

## Command Path Explanation

A proposed command need to be sent on /student_cmd_vel. The command need to be checked by the guard whether it is safe or allowed. If its okay then it will send it to the robot to execute. 

## Graph Explanation

The graph shows the running node in a ros2 system and how they communicate with each other. For example, the /ros_gz_bridge node publishes LiDAR readings on the /scan topic, which can be received by another node such as /course_evidence_collector.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found the ranges field. It represents the lidar distance measurement around the robot. 

## Tools Explanation

Gazebo is responsible for the simulating the robot and its environment. RViz helps displaying data regarding the robots circumstance. 
