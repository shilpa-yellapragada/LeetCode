'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

'''

class Solution(object):
    def sortfunc(self, ele):
        return ele[0] - ele[1]
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        output = sorted(costs,key=self.sortfunc)
        
        n = len(costs)/2
        total = 0
        for i in range(n):
            total += output[i][0] + output[i+n][1]
        return total
