class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx, cover = 0, 0
        if len(nums) == 1:
            return True
        while idx <= cover:
            cover = max(nums[idx] + idx, cover)
            if cover >= len(nums) - 1:
                return True
            idx += 1
            
        return False
