# Mission 3

## Ai Disclosure

I used an AI tool to help me review the mission instructions, explain the required build_pattern implementation, and help create geometry-specific unit tests. I personally reviewed the assigned pattern, changed pattern.py to implement the rounded_rectangle segments, created and corrected test_student_pattern.py, and ran the evaluator. I have verified that the supplied tests passed and used the evaluator results to check my code implementation. The live ROS behavior however remains pending and is not being claimed as verified.

## Assigned Pattern

rounded_rectangle

## Assumptions

The AI assumed that linear velocity is measured in meters per second, angular velocity in radians per second, and duration in seconds. It also assumed that the commanded velocities remain approximately constant during each segment and that the relationship R = v/ω can be used to determine the radius of an arc. It assumed that the robot follows the commanded velocity closely enough for v × t to approximate distance and ω × t to approximate heading change.

## Evidence Analysis

The evaluator tests have establish that the rounded_rectangle pattern is nonempty, it uses valid Segment objects, it also has positive segment duration, and stays within the required linear and angular velocity limits. The supplied tests test_angular_limits, test_linear_limits, test_nonempty, test_pattern_contains_motion, test_pattern_contains_turning, test_positive_duration, and test_segment_types all passed. My student tests additionally checked that the pattern contains eight segments, begins with forward motion, uses left turns, and alternates between straight and turning segments.

These tests do not establish that the robot physically follows the intended rounded-rectangle path in ROS/Gazebo. Live verification is still pending because the ROS run could not complete. Therefore, the actual robot motion, checkpoint poses, and final stopping behavior remain unverified.

One additional test I would need is a successful complete ROS run of the assigned pattern. I would need to verify that the robot follows the expected rounded-rectangle geometry, reaches the expected checkpoint poses, and stops with low velocity at the end of the pattern.

## Live Issue

Why did the robot only move in a circle.


## Live Pending

True

## Modifications

Revision 1
I replaced the `NotImplementedError` in `build_pattern` with eight `Segment` objects representing the required rounded rectangle. I kept the existing `Segment` class and did not modify the ROS wrapper or final-stop behavior.

The four straight segments all use 0.20 m/s. Their durations are 2.00 s for the 0.40 m legs and 1.25 s for the 0.25 m legs. I verified these distances using d = v × t.

The four curved segments use linear velocity 0.12 m/s and angular velocity 0.80 rad/s. This gives an arc radius of 0.15 m because R = v/ω. I calculated the duration as (π/2)/0.80 ≈ 1.9635 s so that each arc produces a 90-degree turn.

Revision 2

I added a `ValueError` for an unknown pattern name so that `build_pattern` rejects patterns other than the assigned `rounded_rectangle` pattern.

Tests/checks used:I checked the segment count and order, the four straight distances, the four 90-degree left turns, the 0.15 m arc radius, and the velocity limits. The planned commands remain below or equal to the required maximum speeds.


## Original Output

Describe the intended sequence, speeds, stopping behavior, and measurable success criteria.



## Original Prompt

Describe the intended sequence, speeds, stopping behavior, and measurable success criteria.



## Original Source

Describe the intended sequence, speeds, stopping behavior, and measurable success criteria.



## Problems

I checked the generated pattern rather than assuming it was correct. I have confirm that it needed eight segments in the required alternating order: straight, turn, straight, turn, straight, turn, straight, turn. I also checked that the straight segments produce the required 0.40 m and 0.25 m distances, that the turns are left turns, and that the angular velocity and duration produce approximately 90-degree turns with a 0.15 m radius.

I also checked the supplied tests for linear and angular velocity limits, positive duration, segment types, motion, and turning. The main uncertainty is live robot behavior. The Python tests establish that the commands meet the mathematical requirements, but they cannot prove that the physical robot follows the intended path or reaches the live checkpoints accurately. Since the ROS run could not complete, I did not claim that live motion or the final stop was verified.

## Saved Specification

Describe the intended sequence, speeds, stopping behavior, and measurable success criteria.



## Specification

Describe the intended sequence, speeds, stopping behavior, and measurable success criteria.



## Test Plan

The mathematical checks do not guarantee that the physical robot will follow the ideal path exactly. Wheel slip, acceleration, controller behavior, timing, and other physical effects could create differences between the commanded and the measured motion. Therefore, I would verify the actual path with the live ROS test rather than assuming the mathematical model guarantees physical performance.

Pattern behavior test: I will try to confirm that the eight commands alternate between forward straight segments and left arcs: 0.40 m, 90° left arc, 0.25 m, 90° left arc, 0.40 m, 90° left arc, 0.25 m, and 90° left arc. The expected result is a rounded-rectangle path that approximately returns to the starting pose after four left arcs.

Velocity-limit test: I will try to check every Segment and verify that the absolute linear velocity is no greater than 0.22 m/s and the absolute angular velocity is no greater than 0.80 rad/s. The expected result is that every command is within the course limits. The planned maximum values are 0.20 m/s linear velocity and 0.80 rad/s angular velocity.

Stop test: I will try to check that the motion wrapper issues a zero-velocity command after the pattern finishes. The expected result is that the robot stops moving after the final segment rather than continuing with the velocity from the final arc.

