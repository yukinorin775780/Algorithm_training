class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1. 确定dp数组含义: dp[i][j]长度为[0,i-1]的字符串text1与长度为[0,j-1]的字符串text2的最长公共子序列长度为dp[i][j]
        2. 确定递推公式: if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1] + 1 
                       else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        3. dp数组初始化: dp[i][0],dp[0][j]=0, 0
        4. 确定遍历顺序: 从左到右从上到下
        5. 打印dp数组
        """

        dp = [[0] * (len(text2)+ 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[len(text1)][len(text2)]1143. 最长公共子序列
