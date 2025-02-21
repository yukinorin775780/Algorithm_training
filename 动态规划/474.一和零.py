class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        1. 确定dp数组含义：dp[i][j]表示最多有i个0和j个1的strs的最大子集大小为dp[i][j]
        2. 确定递推公式：dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num] + 1)
        3. dp数组初始化：dp[i][j] = 0
        4. 确定遍历顺序：先物品后倒序遍历背包
        5. 打印dp数组
        """

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zero_num = s.count('0')
            one_num = len(s) - zero_num
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num] + 1)
            
        return dp[m][n]
