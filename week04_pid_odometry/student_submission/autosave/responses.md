# Autosaved responses

- Name: Raymond Zhang
- Student ID: Raymond.Zhang06@login.cuny.edu
- Section: csci 39536

## Check-in answers

### background_compare

the engineer choose the different values for kp, ki, and kd gains. It helps control how strongly the system responds to error, accumulated error, and the rate of change of error. They tune in so the system reaches the target quickly, accurately, and safely. PID is a feedback controller because it uses the system's output and error to decide what orders to follow rather than follow continuously.

### background_social

A car braking system provides a good example. If the controller behaves too aggressively, the brakes may react too much. It might create accidents like braking, jerking, or just an uncomfortable stop. If it takes too long to stop, it will skip stopping point and put people in danger. Engineers have to consider speed, stability, and safety when tuning in.

### odom_background_wheels

Turns left because \(d_R=6\) and \(d_L=0\), so \(\Delta\theta=(d_R-d_L)/L=6/L>0\), meaning the robot turns left.

### m3_prediction

Increasing speed may increase tracking error and make it harder for the robot to follow the curve precisely.

Too little derivative control may cause overshoot and oscillation during turns.

Therefore clearance may decrease because the robot can drift farther from the planned path and get closer to the pedestrians.

### m3_technical

I predicted that higher speed or too little derivative control could cause more tracking error and create more problems for pedestrians.

The robot computes the direction to the next route point and compares it with its estimated heading to create a heading error.

The PID uses that heading error to adjust the wheel speeds and steer the robot toward the correct route.

The green and orange paths showed some difference between the robot’s true path and its estimated path, with a maximum path error of 0.11 m.

### m3_human

The most consequential failure for a pedestrian would be the robot getting too close to or colliding with a person because of tracking error. I would choose a slower speed and maintain a larger clearance margin, even if that makes the route take longer. Before deployment, the robot's safety settings, route, calibration, and test results should be checked by the responsible engineering or safety team to make sure the system meets the required clearance and tracking limits.

## Mission explanations

### mission_3

**technical_analysis**: I predicted that higher speed or too little derivative control could cause more tracking error and create more problems for pedestrians.

The robot computes the direction to the next route point and compares it with its estimated heading to create a heading error.

The PID uses that heading error to adjust the wheel speeds and steer the robot toward the correct route.

The green and orange paths showed some difference between the robot’s true path and its estimated path, with a maximum path error of 0.11 m.

**human_centered_analysis**: The most consequential failure for a pedestrian would be the robot getting too close to or colliding with a person because of tracking error. I would choose a slower speed and maintain a larger clearance margin, even if that makes the route take longer. Before deployment, the robot's safety settings, route, calibration, and test results should be checked by the responsible engineering or safety team to make sure the system meets the required clearance and tracking limits.
