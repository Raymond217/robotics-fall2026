# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Raymond Zhang
- Email: raymond.zhang06@login.cuny.edu

## final.architecture_evidence

My node is reactive  because it responds directly to the latest lidar measurement and updates the information. it receives /scan and uses the info to decide whether to move or stop. I would add a higher system that controls state, plans, and map management. It would create automatic obstacle-avoidance behavior for immediate safety. 

## final.course_reflection

This activity made me more interested in robotics because I could see how programming concepts are connected to a physical system. Instead of writing code that produces an output on a screen. I was writing behavior that could control a robot's movement based on sensor information. I found the connection between lidar data, python functions, ROS 2 topics, and gazebo fun and interesting. 

The activity also showed me that robotics requires more than simply making the robot perform its intended task. Safety has to be considered at many levels. For example, invalid sensor need to cause the robot to stop, a watchdog handles missing sensor updates, and the command guards check unsafe velocity commands. This made me realize that reliable engineering requires  excellent planning for situations where software or sensors do not behave as expected. 

I would be interested in doing greater projects in the future because they combine programming, problem solving, and engineering. I especially like the idea of building system where different software components communicate and work together to accomplish a larger goal. 

What should out most to me was the ros 2 graph. Seeing how nodes and topics connect made it easier to understand that a robot cannot controlled by one program alone. It is a collection of components that must communicate correctly and safely. This experience showed me the importance of human safety and reliability when designing computing systems that interact with the real world. 

## final.hardware_next

Before using the behavior on real hardware, I would test many LiDAR conditions, including different types of obstacles, invalid readings, missing scans, and different standard of measurement. I would test different velocity limits, communication failures, command timeouts, and emergency stopping. Finally, I would test the system at very low speeds in a controlled environment before moving on to difficult settings. 

## final.middleware_debugging

I would trace the ROS graph and commands like ros2 node info and ros2 topic info --verbose to trace the command through the system. I would check whether the behavior node is publishing to /student_cmd_vel, whether the command guard is subscribed to it, whether it is published to /cmd_vel, and whether the ros-gazebo bridge receives /cmd_vel. This would help identify the exact communication link where the command stopped. 

## final.system_synthesis

Robotics software is difficult because a robot must interact with a changing physical environment while multiple software components interact with each other. Any problems with the operations or gathering information can affect the robot's behavior and safety. The robot cannot just get a command and move. The Sensor data must be processed and coordinated with the command. If conditions are right will the command be executed. 

I implemented a coordinate architecture. My front_distance() takes lidar readings from the front of the robot and compute the nearest measurement. The decide_velocity() function then converts that measurement into either a forward speed or a stop command. The advantage of this architecture is that it is simple and responds quickly to the current sensor input. However, it has major limitation: it does not maintain a longer-term plan or reason about goals, maps, or previous states. It would be better to excellent self-planning and state-based component. 

Ros 2 middleware connected multiple components using topics. The ./obstacle_guard node subscribed to /scan, which carried lidar data, and published proposed commands on /student_cmd_vel. The command guard subscribed  to /student_cmd_vel and publish the approve commands on /cmd_vel. The /ros_gz_bridge connected the ROS 2 system to Gazebo by receiving /cmd_vel and publishing sensor information such as /scan and /odom. This created mulitple communications between nodes like: the behavior node, command guard, ROS-Gazebo bridge, and the simulation environment. 

Timing and invalid sensor data also affected safety. My front_distance() function ignores invalid values such as Nan and infinite reading. It helps preserve fuel and  saves the robot from dangerous obstacles. None is return and 0.0 is used to stop the robot. The system also includes a watchdog that checks when the communication time-out. 

The command guard is very important since it can restrict unsafe motion even if a behavior node proposes an unsafe velocity. The layered design showed me that safe robotics depends only only on making correct decisions, but also on having independent protections that can prevent dangerous commands from reaching the robot. 

## final.timing_evidence

The sensor-failure affected my understanding of robot safety the most. If there is no valid front measurement, the robots stops instead of risking itself. The 0.5 second stale-command timeout showed that timing matters because robots should not execute commands if controlling programs or communication fails. 

## mission_1.command_path_explanation

A proposed command need to be sent on /student_cmd_vel. The command need to be checked by the guard whether it is safe or allowed. If its okay then it will send it to the robot to execute. 

## mission_1.graph_explanation

The graph shows the running node in a ros2 system and how they communicate with each other. For example, the /ros_gz_bridge node publishes LiDAR readings on the /scan topic, which can be received by another node such as /course_evidence_collector.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found the ranges field. It represents the lidar distance measurement around the robot. 

## mission_1.tools_explanation

Gazebo is responsible for the simulating the robot and its environment. RViz helps displaying data regarding the robots circumstance. 

## mission_2.measurement_explanation

A curved path usually wastes distance because it require more time than traveling directly to the target area. It require more distance for traveled path the going in a straight line. 

## mission_2.modified_settings

{'linear_x': 0.1, 'angular_z': 0.5, 'duration': 4.0}

## mission_2.motion_comparison

for the first trial my prediction came exactly true. the start to end the distance and the estimated travel path are the same. The directional change is zero. The distance is suppose to be 0.45 but turns out to be .178

## mission_2.prediction_locks

{'straight': '2026-09-11T21:07:28.472517+00:00', 'rotation': '2026-09-11T21:10:28.663764+00:00', 'curve': '2026-09-11T21:14:00.512444+00:00', 'curve_modified': '2026-09-11T21:16:56.142383+00:00'}

## mission_2.predictions

{'straight': 'I predict that the robot should be .45 m in front of its staring point. ', 'rotation': 'it will change direction to the left but its position will be unchanged. ', 'curve': 'I predict the robot will travel along a curved path because both the forward speed and turning speed are nonzero. The robot will move forward while changing its direction. ', 'curve_modified': 'I predict the robot will move in a tighter curved path. The turning speed is positive, the robot will turn left while it moves forward, creating a curved path rather than traveling straight. '}

## mission_2.safety_explanation

The command guard need to limit speeds to save energy and cancel invalid values. The final zero command helps stop the robot at the designated time and area. The robot needs the timeout to make sure there are no accidents since it is no longer getting orders. 

## mission_3.data_to_command

The front_distance() record only valid measurements within the front sector of the robot. It returns the closest valid distance. Then, decide_velocity() uses the distance to decide whether the robot should move or stop. If there is no valid measurement or an obstacle is there, it returns 0.0. Otherwise the speed is 0.18 m/s.

## mission_3.missing_data_safety

The robot stops when there is no valid measurement because the system cannot confirm that the path is clear. Treating missing or invalid sensor data as clear could cause the robot to move toward the obstacle creating a error. Stopping is the  safer choice. 

## mission_3.system_layers

The supplied ROS node receives lidar data from /scan and passes the reading to front_distance(). The result is passed to decide_velocity(), which produces a forward speed, and the ROS node publishes that proposed command on /student_cmd_vel. The command guard receives the proposed command and moves forwar if it is safe. It then publishes it on /cmd_vel. The result is used to move the robot. 

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
