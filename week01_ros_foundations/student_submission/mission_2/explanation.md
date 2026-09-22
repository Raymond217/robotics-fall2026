# Mission 2

## Predictions

{'straight': 'I predict that the robot should be .45 m in front of its staring point. ', 'rotation': 'it will change direction to the left but its position will be unchanged. ', 'curve': 'I predict the robot will travel along a curved path because both the forward speed and turning speed are nonzero. The robot will move forward while changing its direction. ', 'curve_modified': 'I predict the robot will move in a tighter curved path. The turning speed is positive, the robot will turn left while it moves forward, creating a curved path rather than traveling straight. '}

## Prediction Locks

{'straight': '2026-09-11T21:07:28.472517+00:00', 'rotation': '2026-09-11T21:10:28.663764+00:00', 'curve': '2026-09-11T21:14:00.512444+00:00', 'curve_modified': '2026-09-11T21:16:56.142383+00:00'}

## Motion Comparison

for the first trial my prediction came exactly true. the start to end the distance and the estimated travel path are the same. The directional change is zero. The distance is suppose to be 0.45 but turns out to be .178

## Measurement Explanation

A curved path usually wastes distance because it require more time than traveling directly to the target area. It require more distance for traveled path the going in a straight line. 

## Safety Explanation

The command guard need to limit speeds to save energy and cancel invalid values. The final zero command helps stop the robot at the designated time and area. The robot needs the timeout to make sure there are no accidents since it is no longer getting orders. 

## Modified Settings

{'linear_x': 0.1, 'angular_z': 0.5, 'duration': 4.0}
