class Solution:
    # 与最长公共子序列类似，如果最长公共子序列的长度与s相等，那么就说明是子序列
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[len(s)][len(t)] == len(s)
