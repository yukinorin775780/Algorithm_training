# 方法1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. 确定dp[i]定义：到达下标i的位置所需要的花费为dp[i]
        2. 确定递推公式：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        3. 初始化dp[i]: dp[0] = 0, dp[1] = 0
        4. 确定遍历顺序：从前到后
        5. 打印dp数组
        """
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[len(cost)]

# 方法2
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0, dp1 = 0, 0
        for i in range(2, len(cost)+1):
            dpi = min(dp1 + cost[i-1], dp0 + cost[i-2])
            dp0 = dp1
            dp1 = dpi       
        return dp1
