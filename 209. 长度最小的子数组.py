# 滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = float('inf')
        cur_sum = 0 # 当前累加值

        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum >= target: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1

        return min_len if min_len != float('inf') else 0
