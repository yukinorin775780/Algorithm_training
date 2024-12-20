# 左闭右闭
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # 定义target在左闭右闭的区间里，即: [left, right]

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle - 1 # target 在左区间，所以[left, middle - 1]
            elif nums[middle] < target:
                left = middle + 1 # target 在右区间，所以[middle + 1, right]
            else:
                return middle # 找到目标值，返回下标
        return -1 # 未找到目标值 

# 左闭右开
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) # 定义target在左闭右开的区间里，即: [left, right)

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle # target 在左区间，所以[left, middle)
            elif nums[middle] < target:
                left = middle + 1 # target 在右区间，所以[middle + 1, right)
            else:
                return middle # 找到目标值，返回下标
        return -1 # 未找到目标值 
