# 方法1: 空间复杂度O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1. 确定dp[i]的含义：达到第i阶有dp[i]种方法
        2. 确定递归公式：dp[i] = dp[i-1] + dp[i-2]
        3. dp数组初始化：dp[1] = 1, dp[2] = 2
        4. 确定遍历顺序：从前向后
        5. 打印dp数组
        """
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


# 方法2: 空间复杂度O(3)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total

        return dp[2]
