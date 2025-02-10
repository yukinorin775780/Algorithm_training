class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')  # 初始化结果为无穷小
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 取区间累计的最大值，相当于不断确定最大子序列的终止位置
                result = count
            if count < 0:   # 相当于重置最大子序列的其实位置，因为遇到负数一定是拉低总和
                count = 0
        
        return result
