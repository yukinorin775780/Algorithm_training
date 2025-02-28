class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i][0]表示第i天持有股票的状态下的最大现金
                         dp[i][1]表示第i天保持卖出股票状态下的最大现金
                         dp[i][2]表示第i天卖出股票状态下的最大现金
                         dp[i][3]表示第i天是冷冻期状态下的最大现金
        2. 确定递推公式: dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][3] - prices[i])
                       dp[i][1] = max(dp[i-1][1], dp[i-1][3])
                       dp[i][2] = dp[i-1][0] + prices[i]
                       dp[i][3] = dp[i-1][2]
        3. dp数组初始化: dp[0][0] = - prices[0] 
                       dp[0][1] = 0
                       dp[0][2] = 0
                       dp[0][3] = 0
        4. 确定遍历顺序: 从前到后
        5. 打印dp数组
        """

        if len(prices) == 0:
            return 0
        
        dp = [[0] * 4 for _ in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][3] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        
        return max(dp[len(prices)-1][1] , dp[len(prices)-1][2], dp[len(prices)-1][3])
