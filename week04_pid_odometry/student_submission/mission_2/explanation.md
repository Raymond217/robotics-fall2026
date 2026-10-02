# mission_2 Submission

- Name: Raymond Zhang
- Section: csci 39536

## Explanations

### prediction

The final estimated pose will show an overestimated forward displacement and an underestimated sideways displacement.

### calibration_analysis

I predicted that the forward estimate would be too large when the forward pod scale was too large, and the sideways estimate would be too small when the strafe pod scale was too small.

The forward scale changed  how encoder ticks were converted into forward distance, affecting the robot’s estimated x-position.

The sideways pod is needed because a holonomic robot can move sideways, so a perpendicular tracking pod is needed to measure its y-position accurately.

The remaining drift can happen because of small encoder errors, wheel slip, and imperfections in the robot’s movement and calibration.