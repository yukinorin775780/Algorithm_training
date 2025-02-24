# 一维
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[j]表示装满背包容量为j的背包有dp[j]种方法
        2. 确定递推公式: dp[j] += dp[j-coins[i]]
        3. dp数组初始化: dp[0] = 1
        4. 确定遍历顺序: 先物品后顺序背包 -> 组合数
        5. 打印dp数组
        """
        dp = [0] * (amount + 1)

        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j-coins[i]]
        
        return dp[amount]



# 二维
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        
        return dp[len(coins)-1][amount]
