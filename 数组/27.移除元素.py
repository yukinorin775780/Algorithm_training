class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0 # 快慢指针
        while fast < len(nums):
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把则覆盖 slow 以达到删除的效果
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
