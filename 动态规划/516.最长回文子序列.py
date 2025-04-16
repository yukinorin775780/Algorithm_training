class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        1. dp数组的含义: dp[i][j]表示区间[i,j]的回文子序列的长度
        2. 确定递推公式: if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2 else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        3. dp数组初始化: dp[i][i] = 1
        4. 确定遍历顺序: 从下到上从左到右
        5. 打印dp数组
        """

        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][-1]
