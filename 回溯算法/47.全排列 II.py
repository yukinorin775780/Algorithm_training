class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums, used, [], result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]: # 树层去重
                continue
            if used[i] == True: # 跳过取过的数
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, used, path, result)
            used[i] = False
            path.pop()
