'''
A dieter consumes calories[i] calories on the i-th day. 

Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

If T < lower, they performed poorly on their diet and lose 1 point; 
If T > upper, they performed well on their diet and gain 1 point;
Otherwise, they performed normally and there is no change in points.
Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

Note that the total points can be negative.

Example 1:

Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0
Explanation: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
calories[0] and calories[1] are less than lower so 2 points are lost.
calories[3] and calories[4] are greater than upper so 2 points are gained.
'''
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        if k <= len(calories):
            total_k = sum(calories[0:k])
            if total_k > upper :
                points += 1
            elif total_k < lower:
                points -= 1  
                
            for i in range(1,len(calories)-k+1):
                total_k = total_k - calories[i-1] + calories[i+k-1]
                if total_k > upper :
                    points += 1
                elif total_k < lower:
                    points -= 1
        return points
