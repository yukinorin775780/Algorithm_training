# 使用字典
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for index, value in enumerate(nums):
            # 遍历当前元素，并在map中寻找是否有匹配的key
            if target - value in records:
                return[records[target-value], index]
            # 如果没找到匹配对，就把访问过的元素和下标加入到map中
            records[value] = index
        return []

# 使用集合
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建集合保存见过的数字
        seen = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)

# 使用双指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 对输入的数组进行排序
        nums_sorted = sorted(nums)

        # 使用双指针
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            cur_sum = nums_sorted[left] + nums_sorted[right]
            if cur_sum == target:
                # 如果和等于目标数，则返回两个数的下标
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                if left_index == right_index:
                    # 数组切片，从left + 1 后开始寻找与 nums_sorted[right] 相等的数的下标，由于切片，所以还得加上 left_index+1
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif cur_sum < target:
                # 如果总和小于目标，则将左侧指针向右移动
                left += 1
            else:
                # 如果总和大于目标，则将右侧指针向左移动
                right -= 1

