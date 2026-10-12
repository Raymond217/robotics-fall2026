# Mission 2

## comparison

I tested three moving-average windows while keeping Sensor A's weight at 0.75. With a window of 3, the error was 0.19 m and the delay was 0.25 seconds. In the window of 6, the error dropped to 0.15 m and the delay increased to 0.50 seconds. In the window of 9, the error dropped to 0.13 m, but the delay increased to 0.75 seconds. This shows that larger windows reduce noise but make the system respond more slowly.

I also compared a median filter and a moving-average filter using a window of 5 and the same weight. The median filter had an error of 0.17 m and a maximum error of 0.55 m. The moving average had a slightly lower error of 0.16 m, but its maximum error was higher at 0.85 m. Both had the same delay of 0.42 seconds. Overall, the median filter handled sudden outliers better, while the moving average had slightly lower average error.

## fusion_choice

I tested three different weights for Sensor A while keeping the exponential filter settings the same (window 1 and alpha 0.6). When Sensor A had a weight of 0.5, the RMSE was about 0.17 m, the worst-case error was 0.90 m, and the delay was 0.55 seconds. Sensor B updates only every 0.2 seconds, so it responds more slowly when the distance changes suddenly.

When Sensor A had a weight of 0.9, the RMSE increased to 0.19 m, the worst-case error increased to 1.10 m, and the delay decreased to 0.35 seconds. This happened because Sensor A is noisy, and its sudden spikes, such as 3.91 m, 1.44 m, and 0.26 m, affected the final estimate more.

The best result came from giving Sensor A a weight of 0.75 and Sensor B a weight of 0.25. This setting had an RMSE of 0.148 m, a worst-case error of 0.768 m, and a delay of 0.4 seconds. It was the only setting that gave all three requirements. Sensor A changes quickly every 0.05 seconds, while Sensor B provides smoother readings but updates the content more slowly. Giving Sensor A a weight of 0.75 keeps the system responsive while still using Sensor B to reduce the effect of sudden spikes. Based on my tests, this was the best balance between accuracy and speed.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

 predict that a window of 9 readings will reduce noise but increase response delay compared with a window of 3. An exponential alpha of 0.60 should provide a balance between smoothing and responsiveness. Giving Sensor A a weight of 0.75 will make the estimate more sensitive to noise and outliers than giving more weight to Sensor B.




## responsiveness

The response delay increased from 0.25 seconds with a window of 3 to 0.75 seconds with a window of 9. My own chosen setup had a delay of 0.4 seconds. A smaller window responds faster but lets more noise through, which can cause more error. A larger window reduces noise and error but responds more slowly to changes. This delay can be important for robots and safety systems. For example, if a person walks at 1 m/s, a delay of 0.4 seconds means they move 0.4 meters before the system catches up. At 2 m/s, they move 0.8 meters. Even though my chosen setup meets the 1.25-second delay requirement, a delay can still be risky when a robot needs to react quickly.

## selected

0
