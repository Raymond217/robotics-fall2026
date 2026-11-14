# Week 6: SLAM and Mapping

- email: Raymond.Zhang06@login.cuny.edu
- name: Raymond Zhang

## final.course_reflection

This lab helped me understand how robotics combines programming, sensors, and engineering to get around certain situations in the real world. I found it interesting to watch the turtlebot3 create a map of the world using the surroundings using LiDAR and slam. Before the activity, I though that robots can navigate environment of its own, but this lab taught me how robots measure their positions and avoid certain obstacles. 

One of the most interesting parts is comparing the two road maps. I learned that the route a robot follows can affect how efficiently it maps the environment. I also realized that even when a map looks complete, some areas are not looked because sensors cannot detect everything. 

This experience increased by interest in robotics and artificial intelligence because it showed me how software and physical systems act to work together. I can see how slam technology could be useful in autonomous vehicles, warehouse robots, and robots that assist people in everyday environments. 

Safety and reliability comes first when designing robots. A robot must recognize obstacles, record probabilities, and avoid making mistakes in measuring the environment. Overall this activity helped me appreciate the challenges of autonomous navigation and motivate me to continue learning. 

## final.synthesis

In the lab, I learned how slam allow a robot to create a map of unknown environment while calculating its position. The TurtleBot3 robot used odometry and LiDAR measurements to explore a simulated house created by gazebo. Odometry provided an estimate of the robot's position and operation while LiDAR measured distances to nearby walls and obstacles. SLAM toolbox combined this information to create an occupancy-grid map, which I observed using RViz. 

During mission 1, I follow a route that helps explore areas of the house before moving into the interior. I used the keyboard teleoperation to navigate through accessible corridors and rooms while avoiding walls and furniture. Some areas remained unknown because the robot cannot scan behind certain corridors and corners. 

During mission 2, I used a different strategy by exploring the central corridors and rooms first before moving outside. This allowed me to compared how different exploration routes affect map coverage and efficiency. I examined the wall outlines, unexplored regions, and record the mapping to check both strategies. 

Overall, this lab demonstrated that successful mapping depends on accurate sensor measurement, motion estimates and careful navigation. I learned that a map can appear complete while still containing errors or unknown areas. SLAM helps robots navigate environments and evaluate map quality.

## mission_1.drift_and_revisit

When I returned to a previously explored area, I could compare the new LiDAR scans with the existing walls in RViz. However, I could not clearly determine whether the old walls shifted or doubled. I would need clearer screenshots from before and after revisiting the area to confirm whether SLAM corrected any drift. Therefore, I cannot confidently claim that loop closure occurred.

## mission_1.limitations

An area that remained poorly mapped was near the corners and behind some obstacles in the house. These areas appeared gray or had incomplete wall outlines in RViz. This happened because my robot did not travel close enough to scan every corner, and the LiDAR could not detect objects hidden behind walls or furniture. As a result, some areas remained unknown.

## mission_1.route.original_prediction

My plan is to start near the center left of the house and move into the opening door in the center. I will move up to enter the house. I will then explore the left and right sides of the house. I drive the turtleBot3 through the accessible corridors and rooms,I will use Gazebo to avoid walls and furniture while watching RViz to build the map using LiDAR scans. I will move around corners and obstacles to reveal unknown areas. Finally, I will return to a recognizable junction to check the accuracy of the map.

## mission_1.route.prediction_draft

My plan is to start near the center left of the house and move into the opening door in the center. I will move up to enter the house. I will then explore the left and right sides of the house. I drive the turtleBot3 through the accessible corridors and rooms,I will use Gazebo to avoid walls and furniture while watching RViz to build the map using LiDAR scans. I will move around corners and obstacles to reveal unknown areas. Finally, I will return to a recognizable junction to check the accuracy of the map. 

## mission_2.comparison

In mission 1, I explored the environment by following the outer walls first before moving into the interior. In mission 2, I explored the central corridors and accessible rooms first before moving to the left and right sides. The two strategies allow me to explore the environment in different ways. I compared the maps by examining the perimeter of the walls, the amount of unexplored space, and the alignment of LiDAR scans with previously mapped structures. I also compared the time required to scan each map. These observation helped me determine which route provided a useful map more efficiently. 

## mission_2.map_choice

I would choose the map from mission 1 because it provides a more useful representation of available environment. The map shows a simple house with easy to explore corridors and unknown areas. Compared with the other map, it was easier to explore. The mapping time was 8 minutes compared to 10 minutes for the other map. Based on the map quality and the time required, I consider this strategy the better choice for this environment. 

## mission_2.strategy.original_prediction

For the second route, I plan to start at the robot's original starting position near the center-left of the house. Unlike the first route, I will explore the central corridors and accessible rooms first, then move toward the left and right sides of the house. I will use Gazebo to avoid walls and furniture while monitoring RViz to observe how LiDAR scans create the occupancy-grid map. I will move slowly around corners and obstacles to help the robot avoid walls and detect previously unexplored areas. Finally, I will return to a recognizable wall or junction to check whether the new LiDAR scans align with the mapped walls. I will record the time taken and compare the completeness and quality of this map with my Mission 1 map.

## mission_2.strategy.prediction_draft

For the second route, I plan to start at the robot's original starting position near the center-left of the house. Unlike the first route, I will explore the central corridors and accessible rooms first, then move toward the left and right sides of the house. I will use Gazebo to avoid walls and furniture while monitoring RViz to observe how LiDAR scans create the occupancy-grid map. I will move slowly around corners and obstacles to help the robot avoid walls and detect previously unexplored areas. Finally, I will return to a recognizable wall or junction to check whether the new LiDAR scans align with the mapped walls. I will record the time taken and compare the completeness and quality of this map with my Mission 1 map. 

