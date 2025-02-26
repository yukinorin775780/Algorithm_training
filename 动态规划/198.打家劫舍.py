class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. 确定dp数组定义: 考虑下标i(包括i)以内的房屋，最多可以偷窃的金额为dp[i]
        2. 确定递推公式: dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 
        3. dp数组初始化: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        4. 确定遍历顺序: 
        5. 打印dp数组
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[len(nums) - 1]
