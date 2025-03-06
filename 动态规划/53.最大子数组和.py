class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i]表示包括下标i的最大连续子序列和为dp[i]
        2. 确定递推公式: dp[i] = max(dp[i-1] + nums[i], nums[i])
        3. dp数组初始化: dp[0] = nums[0]
        4. 确定遍历顺序: 从左到右
        5. 打印dp数组
        """

        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(dp[i], result)

        return result
