class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. 确定dp数组含义: dp[j]表示长度为j的字符串能否被拆分为一个或多个字典中出现的单词是dp[j]
        2. 确定递推公式: if s[i,j] 在字典里 and dp[i]== True -> dp[j] = True 
        3. dp数组初始化: dp[0] = True, dp[j] = False
        4. 确定遍历顺序: 先顺序遍历背包后遍历物品 -> 排列数
        5. 打印dp数组
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(1, len(s) + 1):  # 先顺序遍历背包
            for word in wordDict:   # 后遍历物品
                if j >= len(word):  # 背包大小可容纳当前物品时
                    dp[j] = dp[j] or (dp[j-len(word)] and word == s[j-len(word):j])
        
        return dp[len(s)]
