# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i][0]表示第i天持有股票所得最多现金
                         dp[i][1]表示第i天不持有股票所得最多现金
        2. 确定递推公式: dp[i][0] = max(dp[i-1][0], -prices[i]); 
                       dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        3. dp数组初始化: dp[0][0] = -price[0]; dp[0][1] = 0
        4. 确定遍历顺序: 从前往后遍历
        5. 打印dp数组
        """
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[length-1][1]


# 贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        
        return result
