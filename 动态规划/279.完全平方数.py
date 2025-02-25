class Solution:
    def numSquares(self, n: int) -> int:
        """
        1. 确定dp数组含义: dp[j]表示和为n的完全平方数的最少数量为dp[j] 
        2. 确定递推公式: dp[j] = min(dp[j], dp[j - i * i] + 1)
        3. dp数组初始化: dp[0] = 0, dp[j] = float('inf')
        4. 确定遍历顺序: 先物品后顺序遍历背包 -> 组合数 / 先顺序遍历背包后物品 -> 排列数
        5. 打印dp数组
        """

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, int(n ** 0.5) + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        
        return dp[n]
