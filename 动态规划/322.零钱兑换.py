class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1. 确定dp数组的含义: dp[j]表示凑足金额为j所需钱币的最少个数为dp[j]
        2. 确定递推公式: dp[j] = min(dp[j-coins[i]] + 1, dp[j])
        3. dp数组的初始化: dp[0] = 0, dp[j] = float('inf')
        4. 确定遍历顺序: 先遍历物品后顺序遍历背包 -> 组合数/ 先顺序遍历背包后遍历物品 -> 排列数
        5. 打印dp数组
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
    
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
