# Mission 3

## Assistive.prediction_draft

I predict that scenarios with missing sensor readings, sudden changes in distance, and people close to the robot will be the most challenging. The safety distance is 0.95 m, therefore the robot needs to respond carefully when someone is nearby. I expect a more cautious policy can reduce unsafe movement, but it may create more unnecessary stops and longer detection delays. I will test all seven different scenarios and compare the results with the original policy. 


## Warehouse.prediction_draft

I predict that scenarios that have robots with missing sensor readings, sudden changes in distance, and obstacles close to the robot will be the most challenging. Compared with previous policy, I expected the new policy to prevent dangerous decision. However I may cause more unnecessary stops or longer detection delays. I will compare the results from all seven scenarios to see whether the revised policy improves safety. 

## context_comparison

The Warehouse and Assistive policies use different settings because they have different needs. The Warehouse policy uses a bigger stopping margin, helping the robot stop earlier to protect workers and equipment. However, this could create more unnecessary stops. The Assistive policy uses a smaller margin, which may allow help to continue more smoothly but leaves less room for safety. The policies also use different confirmation counts. More confirmations can prevent decisions based on unreliable readings, but they can delay the robot's response. In my tests, the Warehouse policy had an RMSE of about 0.05 m and 3 insufficient results. The Assistive policy had an RMSE of about 0.04 m and 0 insufficient results.


## error_costs

In a warehouse, a false-safe decision can cause the robot to injure a worker or damage equipment. An unnecessary stop can slow down work and deliveries. In the assistive setting, a false-safe decision can injure someone receiving care. Unnecessary stops can delay help and frustrate both the person and caregiver. The warehouse baseline had 0 false-safe decisions, 0 unnecessary stops, 3 insufficient results, and an RMSE of about 0.05 m. The revised assistive policy had 0 false-safe decisions, 0 unnecessary stops, 0 insufficient results, and an RMSE of about 0.04 m. Both policies avoided dangerous commands in these tests, but more testing is needed to confirm their safety.

## limitations

The seven tests showed that both policies had 0 false-safe decisions and 0 unnecessary stops in the tested situations. The Warehouse policy has reported insufficient three times when both sensors lost their readings. The Assistive policy had an RMSE of about 0.04 m. However, these tests do not prove the policies will be safe in every situation, such as during long sensor failures or sudden movements. Before deployment, I would consult a warehouse safety specialist and a caregiver. I would also test what happens when both sensors lose their readings for one second while a person is nearby. This would help determine whether the robot can respond safely when sensor information is missing.
