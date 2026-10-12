# Week 5: Sensors, Noise, and Uncertainty

- course_id: csci 39536
- email: Raymond.Zhang06@login.cuny.edu
- name: Raymond Zhang

## concepts.observation

When I boosted noise, the readings became more scattered in the plot. The graph became more wider as the variance and standard deviation increased. When I increased bias, the readings moved away from the true actual value. The spread did not change but the mean and median did. Noise changes the consistency of the readings, while bias changes the accuracy. 

## final.course_reflection

This hw help me understand how robotics and real world computing can be used to solve everyday problems. I learned that robots need to make certain decisions even when data and sensor readings are noisy, delayed, or missing. I also learn that changing the setting can affect how a robot accurately perceive its surroundings. It can also affect how quickly the robot responds to certain situations. 

The activity increased my interest in robotics because I could test the different settings and compare the results. It show me that engineering requires far more than just writing code. Engineers must revise their designs, identify new problems, and improve solutions. 

one important lesson is that a robots decision can affect people livelihood and safety. A warehouse robot must ensure the safety of its workers in the warehouse. An assistive robot must take care of patients and other people needed care. An unnecessary stop can cause delays. An calculated unsafe movement can cause injury.  This showed me why engineers must consider both technical results and human needs.
I learned that policies need to be tested to identify their strength and weakness. In the future, I would like to learn more about robotics, programming, and artificial intelligence. I want to understand how technology can be made safer, more reliable, and more helpful to people.

## final.synthesis

Along all three missions, I learned that sensor measurements, estimation methods, and the robot’s surroundings are critical for making safe decisions.
For mission 1, I analyzed sensor accuracy and reliability. My sensor reading had a mean of 1.9859 m when the actual distance is 2.00 m, giving a bias of -0.0141 m. It showed that the sensor was slightly inaccurate on the average. I also identified missing data points and some outliers, showing why sensor data must be checked before it is used. 
In mission 2, I was tasked with comparing filtering methods and sensor fusion. Using the exponential filter with Sensor A weighted at 0.75 and Sensor B at 0.25 gave an RMSE of about 0.148 m, a maximum error of 0.768 m, and a response delay of 0.4 seconds. This provided a excellent balance between accuracy and responsiveness because Sensor A updated faster while Sensor B provided steadier readings. 
In mission 3, I learned that robot decision must match the situation. A warehouse robot must protect workers and equipment while preventing unnecessary delays. An assistive robot must put the safety of people receiving help first. My tests showed zero false-safe decisions in the tested scenarios but more testing is required before deployment. 
Overall, reliable robots require good measurements, suitable estimation methods, and safety policies designed for the people who may be affected.

## mission_1.bias

-0.0141 

## mission_1.bias_vs_variance

Bias measures how far the average data point is from the true distance, while variance measures how spread out the data points are. My sensor had a small bias of -0.0141 m and a variance of 0.00431 m², meaning most readings were close to the true distance of 2.00 m.

## mission_1.dropouts

6

## mission_1.mean

1.9859 

## mission_1.median

2.00

## mission_1.more_samples

Taking more samples can help reduce the effect of random noise and make the average more reliable. However, more samples cannot fix overall bias because the sensor would continue making the same error. It also cannot automatically fix missing data points or outliers. 

## mission_1.outliers

1

## mission_1.prediction

A biased sensor would give readings consistently above or below 2.00 m, the mean will be far from the true value. A noisy sensor would give reading that are scattered above and below 2.00 m, creating a higher standard deviation and variance, but the mean would stay close to 2.00m.

## mission_1.prediction_draft

A biased sensor would give readings consistently above or below 2.00 m, the mean will be far from the true value. A noisy sensor would give reading that are scattered above and below 2.00 m, creating a higher standard deviation and variance, but the mean would stay close to 2.00m.

## mission_1.profile

quantized

## mission_1.robot_consequence

If a robot uses the sensor to detect certain obstacles. It would cause inaccurate readings could cause it to misjudge distances. For example, the outlier of 1.10 m could make the robot think an obstacle is much closer than it really is, causing it to stop or change wrong direction.

## mission_1.variance

0.00431 

## mission_2.comparison

I tested three moving-average windows while keeping Sensor A's weight at 0.75. With a window of 3, the error was 0.19 m and the delay was 0.25 seconds. In the window of 6, the error dropped to 0.15 m and the delay increased to 0.50 seconds. In the window of 9, the error dropped to 0.13 m, but the delay increased to 0.75 seconds. This shows that larger windows reduce noise but make the system respond more slowly.

I also compared a median filter and a moving-average filter using a window of 5 and the same weight. The median filter had an error of 0.17 m and a maximum error of 0.55 m. The moving average had a slightly lower error of 0.16 m, but its maximum error was higher at 0.85 m. Both had the same delay of 0.42 seconds. Overall, the median filter handled sudden outliers better, while the moving average had slightly lower average error.

## mission_2.fusion_choice

I tested three different weights for Sensor A while keeping the exponential filter settings the same (window 1 and alpha 0.6). When Sensor A had a weight of 0.5, the RMSE was about 0.17 m, the worst-case error was 0.90 m, and the delay was 0.55 seconds. Sensor B updates only every 0.2 seconds, so it responds more slowly when the distance changes suddenly.

When Sensor A had a weight of 0.9, the RMSE increased to 0.19 m, the worst-case error increased to 1.10 m, and the delay decreased to 0.35 seconds. This happened because Sensor A is noisy, and its sudden spikes, such as 3.91 m, 1.44 m, and 0.26 m, affected the final estimate more.

The best result came from giving Sensor A a weight of 0.75 and Sensor B a weight of 0.25. This setting had an RMSE of 0.148 m, a worst-case error of 0.768 m, and a delay of 0.4 seconds. It was the only setting that gave all three requirements. Sensor A changes quickly every 0.05 seconds, while Sensor B provides smoother readings but updates the content more slowly. Giving Sensor A a weight of 0.75 keeps the system responsive while still using Sensor B to reduce the effect of sudden spikes. Based on my tests, this was the best balance between accuracy and speed.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

 predict that a window of 9 readings will reduce noise but increase response delay compared with a window of 3. An exponential alpha of 0.60 should provide a balance between smoothing and responsiveness. Giving Sensor A a weight of 0.75 will make the estimate more sensitive to noise and outliers than giving more weight to Sensor B.




## mission_2.responsiveness

The response delay increased from 0.25 seconds with a window of 3 to 0.75 seconds with a window of 9. My own chosen setup had a delay of 0.4 seconds. A smaller window responds faster but lets more noise through, which can cause more error. A larger window reduces noise and error but responds more slowly to changes. This delay can be important for robots and safety systems. For example, if a person walks at 1 m/s, a delay of 0.4 seconds means they move 0.4 meters before the system catches up. At 2 m/s, they move 0.8 meters. Even though my chosen setup meets the 1.25-second delay requirement, a delay can still be risky when a robot needs to react quickly.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

I predict that scenarios with missing sensor readings, sudden changes in distance, and people close to the robot will be the most challenging. The safety distance is 0.95 m, therefore the robot needs to respond carefully when someone is nearby. I expect a more cautious policy can reduce unsafe movement, but it may create more unnecessary stops and longer detection delays. I will test all seven different scenarios and compare the results with the original policy. 


## mission_3.Warehouse.prediction_draft

I predict that scenarios that have robots with missing sensor readings, sudden changes in distance, and obstacles close to the robot will be the most challenging. Compared with previous policy, I expected the new policy to prevent dangerous decision. However I may cause more unnecessary stops or longer detection delays. I will compare the results from all seven scenarios to see whether the revised policy improves safety. 

## mission_3.context_comparison

The Warehouse and Assistive policies use different settings because they have different needs. The Warehouse policy uses a bigger stopping margin, helping the robot stop earlier to protect workers and equipment. However, this could create more unnecessary stops. The Assistive policy uses a smaller margin, which may allow help to continue more smoothly but leaves less room for safety. The policies also use different confirmation counts. More confirmations can prevent decisions based on unreliable readings, but they can delay the robot's response. In my tests, the Warehouse policy had an RMSE of about 0.05 m and 3 insufficient results. The Assistive policy had an RMSE of about 0.04 m and 0 insufficient results.


## mission_3.error_costs

In a warehouse, a false-safe decision can cause the robot to injure a worker or damage equipment. An unnecessary stop can slow down work and deliveries. In the assistive setting, a false-safe decision can injure someone receiving care. Unnecessary stops can delay help and frustrate both the person and caregiver. The warehouse baseline had 0 false-safe decisions, 0 unnecessary stops, 3 insufficient results, and an RMSE of about 0.05 m. The revised assistive policy had 0 false-safe decisions, 0 unnecessary stops, 0 insufficient results, and an RMSE of about 0.04 m. Both policies avoided dangerous commands in these tests, but more testing is needed to confirm their safety.

## mission_3.limitations

The seven tests showed that both policies had 0 false-safe decisions and 0 unnecessary stops in the tested situations. The Warehouse policy has reported insufficient three times when both sensors lost their readings. The Assistive policy had an RMSE of about 0.04 m. However, these tests do not prove the policies will be safe in every situation, such as during long sensor failures or sudden movements. Before deployment, I would consult a warehouse safety specialist and a caregiver. I would also test what happens when both sensors lose their readings for one second while a person is nearby. This would help determine whether the robot can respond safely when sensor information is missing.
