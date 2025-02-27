class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i][1]表示第一次持有股票所剩的最大现金
                         dp[i][2]表示第一次不持有股票所剩的最大现金
                         dp[i][3]表示第二次持有股票所剩的最大现金
                         dp[i][4]表示第二次不持有股票所剩的最大现金
        2. 确定递推公式: dp[i][1] = max(dp[i-1][1], 0 - prices[i])
                       dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
                       dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
                       dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        3. dp数组初始化: dp[0][1] = - prices[i] 
                       dp[0][2] = 0
                       dp[0][3] = -prices[i] 
                       dp[0][4] = 0
        4. 确定遍历顺序: 从前到后
        5. 打印dp数组
        """
        if len(prices) == 0:
            return 0
        
        dp = [[0] * 5 for _ in range(len(prices))]
        
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[-1][4]
