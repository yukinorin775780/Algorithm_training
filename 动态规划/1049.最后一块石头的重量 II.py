# 一维
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        1. 确定dp数组含义：dp[j]表示容量为j的背包，最多可以背最大重量为dp[j]
        2. 确定递推公式： dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
        3. dp数组初始化：dp[j] = 0
        4. 确定遍历顺序：先物品，后倒叙遍历背包
        5. 打印dp数组
        """
        total_sum = sum(stones)
        target = total_sum // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j-stone]+stone)
        
        return total_sum - dp[target] - dp[target]

