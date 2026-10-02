# mission_1 Submission

- Name: Raymond Zhang
- Section: csci 39536

## Explanations

### prediction

Too little Kp makes the arm react too slow and settle with a large error. Too little Kd causes overshoot and oscillation because there  isn't enough damping to control it.

### tuning_analysis

I increased Kp to make both joints respond strongly to the targets and used Kd to reduce overshoot and oscillation. The evidence of improvement was that the arm successfully nailed all 3 poses and settled in more smoothly. Gravity compensation helped the shoulder handle the downward force from the arm, making it easier to hold the target position.