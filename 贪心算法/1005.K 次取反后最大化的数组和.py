class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse = True) # 按绝对值降序排序数组
        
        # 执行k次取反操作
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        # 如果k有剩余次数，将绝对值小的元素取反
        if k % 2 == 1:
            nums[-1] *= -1
        
        result = sum(nums)
        return result
