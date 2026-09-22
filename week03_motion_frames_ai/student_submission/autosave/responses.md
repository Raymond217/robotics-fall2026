# Week 3: Motion, Frames, and AI-Assisted ROS Development

## Student

- Course Id: 5485
- Email: Raymond.Zhang06@login.cuny.edu
- Name: Raymond Zhang

## concept.arc

when the robot has both linear velocity and angular velocity . It is moving forward while turning at the same time. 

## concept.model_limits

one assumption is the robot will move at the same speed as input velocity. There are slippery roads, mechanical failures, and errors. 

## concept.velocity_pose

A velocity only tells us how fast the robot moves, but how far the robot will go. We need the duration of how far the robot will move to get the travel distance. 

## mission_1.error_source

The robot might move differently from the equations because of environment and erroneous commands. The robot may actually be near the predicted position but its sensor give wrong direction.

## mission_1.largest_error

There are no record motion results. There are no discrepancy metrics to cite. 

## mission_1.model_vs_observation

The system reports "No motion-sequence evidence found," so there is no evidence for comparison. 

## mission_1.predictions

{'arc': {'theta': 1.6, 'x': 0.375, 'y': 0.365}, 'straight': {'theta': 0.0, 'x': 0.45, 'y': 0.0}, 'turn_then_drive': {'theta': 1.571, 'x': 0.0, 'y': 0.3}}

## mission_1.predictions_locked_at

2026-09-17T18:49:54.474877+00:00

## mission_1.twice_distance

the distance traveled will nearly doubled. 
