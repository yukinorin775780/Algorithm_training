class Solution:
    def numTrees(self, n: int) -> int:
        """
        1. 确定dp数组的含义：1到i为节点组成的二叉搜索树的个数为dp[i]
        2. 确定递推公式：dp[i] += dp[j-1] * dp[i-j]
        3. dp数组初始化：dp[0]=1
        4. 确定遍历顺序：从小到大
        5. 打印dp数组
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
