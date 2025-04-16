class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        1. dp数组的含义: dp[i][j]表示区间[i,j]的子串是否是回文子串
        2. 确定递推公式: if s[i] == s[j]: if j - i <= 1: result+=1 dp[i][j] = true elif(dp[i+1][j-1]): result+=1 dp[i][j]=true
        3. dp数组初始化: dp[i][j] = false
        4. 确定遍历顺序: 从左到右 从下到上
        5. 打印dp数组
        """

        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1): # 注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        result += 1
                        dp[i][j] = True
        
        return result
