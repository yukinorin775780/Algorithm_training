class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        1. dp数组的含义: dp[i][j]表示以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
        2. 确定递推公式: if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j] else: dp[i][j] = dp[i-1][j]
        3. dp数组初始化: dp[i][0] = 1; dp[0][j] = 0; dp[0][0] = 1
        4. 确定遍历顺序: 从上到下从左到右
        5. 打印dp数组
        """

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        for i in range(len(s)):
            dp[i][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1] 
