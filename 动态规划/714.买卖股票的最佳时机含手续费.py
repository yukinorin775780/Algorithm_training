class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        1. 确定dp数组含义: dp[i][0]表示持有股票的最大现金，dp[i][1]表示不持有股票的最大现金
        2. 确定递推公式: dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
                       dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        3. dp数组初始化: dp[0][0] = -prices[0], dp[0][1] = 0
        4. 确定遍历顺序: 从前向后
        5. 打印dp数组
        """
        dp = [[0] * 2 for _ in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        
        return dp[-1][1]
