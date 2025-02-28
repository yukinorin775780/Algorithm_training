class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i][j]表示第i天的状态为j，所剩下的最大现金是dp[i][j]
                         且j为偶数时是卖出的状态，j为奇数时是持有的状态
        2. 确定递推公式: dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                       dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        3. dp数组初始化: j为偶数时，dp[0][j] = -prices[0]
        4. 确定遍历方向: 从前向后
        5. 打印dp数组
        """
        if len(prices) == 0:
            return 0
        
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(0 , 2 * k - 1, 2): # 2 * k 也正确
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        
        return dp[-1][2 * k]
