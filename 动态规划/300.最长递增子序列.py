# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i]表示i之前包括i的以nums[i]结尾的最长递增子序列
        2. 确定递推公式: if nums[i] > nums[j]: dp[i] = max(dp[j] + 1, dp[i])
        3. dp数组初始化: dp[i] = 1
        4. 确定遍历顺序: 从左到右
        5. 打印dp数组
        """
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            
            result = max(result, dp[i])
        return result


# 贪心
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        tails = [nums[0]]   # 存储递增子序列的尾部元素
        for num in nums[1:]:
            if num > tails[-1]:
                tails.append(num)   # 如果当前元素大雨递增子序列的最后一个元素，直接加入到子序列末尾
            else:
                # 使用二分法查找找到当前元素在递增子序列的位置，并替换对应位置的元素
                left, right = 0, len(tails) - 1
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                tails[left] = num
            
        return len(tails)
