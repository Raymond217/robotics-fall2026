# Mission 1

## bias

-0.0141 

## bias_vs_variance

Bias measures how far the average data point is from the true distance, while variance measures how spread out the data points are. My sensor had a small bias of -0.0141 m and a variance of 0.00431 m², meaning most readings were close to the true distance of 2.00 m.

## dropouts

6

## mean

1.9859 

## median

2.00

## more_samples

Taking more samples can help reduce the effect of random noise and make the average more reliable. However, more samples cannot fix overall bias because the sensor would continue making the same error. It also cannot automatically fix missing data points or outliers. 

## outliers

1

## prediction

A biased sensor would give readings consistently above or below 2.00 m, the mean will be far from the true value. A noisy sensor would give reading that are scattered above and below 2.00 m, creating a higher standard deviation and variance, but the mean would stay close to 2.00m.

## prediction_draft

A biased sensor would give readings consistently above or below 2.00 m, the mean will be far from the true value. A noisy sensor would give reading that are scattered above and below 2.00 m, creating a higher standard deviation and variance, but the mean would stay close to 2.00m.

## profile

quantized

## robot_consequence

If a robot uses the sensor to detect certain obstacles. It would cause inaccurate readings could cause it to misjudge distances. For example, the outlier of 1.10 m could make the robot think an obstacle is much closer than it really is, causing it to stop or change wrong direction.

## variance

0.00431 
