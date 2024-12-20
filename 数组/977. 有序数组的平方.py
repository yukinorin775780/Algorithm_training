class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, i = 0, len(nums)-1, len(nums)-1
# 这句代码的意思是创建一个与 nums 列表长度相同的列表 res，并将其中的每个元素初始化为正无穷（float('inf')）。具体来说：
# float('inf') 是 Python 中表示正无穷大的一种方式。
# len(nums) 返回 nums 列表的长度。
# [float('inf')] * len(nums) 创建一个新的列表，其中包含 len(nums) 个 float('inf') 元素。
        res = [float('inf')] * len(nums)
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:  # 左右边界进行比较，找出最大值
                res[i] = nums[right] ** 2
                right -= 1 # 右指针向左移动
            else:
                res[i] = nums[left] ** 2
                left += 1 # 左指针向右移动
            i -= 1 # 存放结果的指针向左移动一位
        return res
