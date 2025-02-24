class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        1. 确定dp数组含义：dp[j]表示凑成正整数j的排列数有dp[j]
        2. 确定递推公式：dp[j] += dp[j-nums[i]]
        3. dp数组初始化：dp[0] = 1
        4. 确定遍历顺序：先顺序遍历背包后遍历物品 -> 排列数
        5. 打印dp数组
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target + 1): # 先遍历背包
            for num in nums:  # 再遍历物品
                if num <= j: # 当物品重量小于等于背包容量时
                    dp[j] += dp[j - num]

        return dp[target]
