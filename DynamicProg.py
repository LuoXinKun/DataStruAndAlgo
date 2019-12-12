
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
		
"""
DP动态规划  
 三要素 1：最优化原理
        2：无后效性
        3：有重叠子问题
比如 零钱找零问题 有1 5 10 三种硬币   f(w) = min(f(w-1),f(w-5),f(w-10))+1
然后从1开始接这个公式堆下去到w
"""

class MinMoneyDP(object):           #最少张数找零
    def __init__(self,moneyArr=None):
        if moneyArr == None:
            self.moneyArr = [1,2,5,10]
        else:
            self.moneyArr = moneyArr

        self.moneyDPList = []

    def dealWith(self,dealArr):   #有时候moneyArr 里面最小单位不是1   会造成无解 所以加了这个
        minNum = -1
        minSub = -1
        for i, num in enumerate(dealArr):
            if num ==0 or num == -1:
                continue
            if minNum == -1:
                minNum = num
            else:
                minNum = min(minNum, num)
        for i, num in enumerate(dealArr):
            if minNum == num:
                minSub = i

        mon = max(dealArr)
        if mon == -1 or mon == 0:
            mon = -1
        else:
            mon = minSub
        return minSub,mon

    def change(self,money,moneyArr=None):
        if moneyArr ==None:
            moneyArr = self.moneyArr

        DPList = [0 for i in range(money+1)]
        minSheet = [0 for i in range(money+1)]

        for num in range(1,money+1):
            tempList = [0 for i in range(len(moneyArr))]
            for i,ml in enumerate(moneyArr):
                if num - ml<0:
                    tempList[i] = -1
                else:
                    tempList[i] = DPList[num-ml]+1
            minSub,mon = self.dealWith(tempList)

            if minSub == -1:
                DPList[num] = -1
            else:
                DPList[num] =tempList[minSub]

            if mon == -1:
                minSheet[num] = -1
            else:
                minSheet[num] = moneyArr[mon]

        print(DPList)
        print(minSheet)
        temMoney = money
        if minSheet[temMoney] == -1:
            return -1
        resultlist = []
        while temMoney>0:
            resultlist.append(minSheet[temMoney])
            temMoney -= minSheet[temMoney]
        return resultlist


mmdp = MinMoneyDP()
print(mmdp.change(28,[1,5,10]))