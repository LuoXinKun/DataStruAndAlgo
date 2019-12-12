
"""

"""

class Solution(object):
    """
    上楼梯
    """
    def climbStairs(self, n):
        if n <=2:
            return n
        a = 1
        b = 2
        temp = 0
        for i in range(3,n+1):
            temp = a+b
            a = b
            b = temp
        return temp
		
		
    """
    爬楼梯体力消耗
    """
    def minCostClimbingStairs(self,cost):
        if len(cost) == 0:
            return 0
        if len(cost)==1:
            return cost[0]
        if len(cost) ==2:
            return min(cost[0], cost[1])
        else:
            dp = []
            dp.append(cost[0])
            dp.append(cost[1])
            for i in range(2, len(cost)+1):
                if i == len(cost):
                    dp.append(min(dp[i-1], dp[i-2]))
                else:
                    dp.append(min(cost[i]+dp[i-1], cost[i]+dp[i-2]))
        return dp[-1]