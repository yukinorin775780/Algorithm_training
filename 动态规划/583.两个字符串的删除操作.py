class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        1. dp数组的含义: dp[i][j]表示 以i-1结尾的字符串word1，和以j-1结尾的字符串word2，达到相等所需要删除元素的最少次数
        2. 确定递推公式: if word[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] else: dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        3. dp数组初始化: dp[i][0] = i, dp[0][j] = j
        4. 确定遍历顺序: 从上到下从左到右
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
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
        
        return dp[-1][-1]



# 方法2: 最长公共子序列
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m +1 ):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return m + n - 2 * dp[-1][-1]
