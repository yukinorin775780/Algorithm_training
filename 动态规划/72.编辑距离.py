class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        1. dp数组的含义: dp[i][j]表示以i-1结尾的word1 和 以j-1结尾的word2，最近的编辑距离为dp[i][j]
        2. 确定递推公式: if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] else: min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
        3. dp数组初始化: dp[i][0] = i, dp[0][j] = j
        4. 确定遍历顺序: 从左到右从上到下
        5. 打印dp数组
        """

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        
        return dp[-1][-1]
