# 方法1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        1. 确定dp数组含义：dp[i][j]代表从(0,0)出发，到(i,j)有dp[i][j]条不同路径
        2. 确定递推公式：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        3. dp数组初始化：dp[i][0] = 1, dp[0][j] = 1
        4. 确定遍历顺序：从左到右从上到下
        5. 打印dp数组
        """
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# 方法2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for j in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]

        return dp[n - 1]

# 递归(超时)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
