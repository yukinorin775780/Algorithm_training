class Solution:
    def fib(self, n: int) -> int:
        """
        1. 确定dp[i]含义：第i个斐波那契数值为dp[i]
        2. 确定递推公式：dp[i] = dp[i-1] + dp[i-2]
        3. dq数组初始化：dp[0] = 1, dp[1] = 1
        4. 确定遍历顺序：从前向后
        5. 打印dp数组（用于debug）
        """
        if n == 0:
            return 0
        
        # 创建dp数组
        dp = [0] * (n+1)
        # 初始化dp数组
        dp[0], dp[1] = 0, 1
        # 遍历顺序：从前向后，因为后面要用到前面的状态
        for i in range(2, n+1):
            # 递推公式
            dp[i] = dp[i-1] + dp[i-2]
        
        # 返回答案
        return dp[n]
