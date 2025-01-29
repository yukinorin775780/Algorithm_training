# 利用 used 数组去重
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums, 0, used, [], result)
        return result

    def backtracking(self, nums, start_index, used, path, result):
        result.append(path[:])
        if start_index >= len(nums):
            return
        
        for i in range(start_index, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, i+1, used, path, result)
            path.pop()
            used[i] = False

# 利用set去重
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtracking(nums, 0, [], result)
        return result

    def backtracking(self, nums, start_index, path, result):
        result.append(path[:])
        uset = set()
        for i in range(start_index, len(nums)):
            # 数层去重
            if nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()

# 利用 start_index 去重
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtracking(nums, 0, [], result)
        return result

    def backtracking(self, nums, start_index, path, result):
        result.append(path[:])
        for i in range(start_index, len(nums)):
            # 树层去重
            if i > start_index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
