# 贪心
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        result = 1  # 连续子序列最小值为1
        count = 1
        
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]: # 连续记录
                count += 1
            else:   # 不连续，count从头开始
                count = 1

            result = max(result, count)
        
        return result


# 动态规划
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i]表示以i为结尾的连续递增子序列长度为dp[i]
        2. 确定递推公式: dp[i] = dp[i-1] + 1
        3. dp数组初始化: dp[i] = 1
        4. 确定遍历顺序: 从前向后
        5. 打印dp数组
        """
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        result = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                dp[i + 1] = dp[i] + 1
            
            result = max(result, dp[i + 1])
        
        return result
