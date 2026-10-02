# mission_3 Submission

- Name: Raymond Zhang
- Section: csci 39536

## Explanations

### technical_analysis

I predicted that higher speed or too little derivative control could cause more tracking error and create more problems for pedestrians.

The robot computes the direction to the next route point and compares it with its estimated heading to create a heading error.

The PID uses that heading error to adjust the wheel speeds and steer the robot toward the correct route.

The green and orange paths showed some difference between the robot’s true path and its estimated path, with a maximum path error of 0.11 m.

### human_centered_analysis

The most consequential failure for a pedestrian would be the robot getting too close to or colliding with a person because of tracking error. I would choose a slower speed and maintain a larger clearance margin, even if that makes the route take longer. Before deployment, the robot's safety settings, route, calibration, and test results should be checked by the responsible engineering or safety team to make sure the system meets the required clearance and tracking limits.