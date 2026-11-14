# Final synthesis

In the lab, I learned how slam allow a robot to create a map of unknown environment while calculating its position. The TurtleBot3 robot used odometry and LiDAR measurements to explore a simulated house created by gazebo. Odometry provided an estimate of the robot's position and operation while LiDAR measured distances to nearby walls and obstacles. SLAM toolbox combined this information to create an occupancy-grid map, which I observed using RViz. 

During mission 1, I follow a route that helps explore areas of the house before moving into the interior. I used the keyboard teleoperation to navigate through accessible corridors and rooms while avoiding walls and furniture. Some areas remained unknown because the robot cannot scan behind certain corridors and corners. 

During mission 2, I used a different strategy by exploring the central corridors and rooms first before moving outside. This allowed me to compared how different exploration routes affect map coverage and efficiency. I examined the wall outlines, unexplored regions, and record the mapping to check both strategies. 

Overall, this lab demonstrated that successful mapping depends on accurate sensor measurement, motion estimates and careful navigation. I learned that a map can appear complete while still containing errors or unknown areas. SLAM helps robots navigate environments and evaluate map quality.
