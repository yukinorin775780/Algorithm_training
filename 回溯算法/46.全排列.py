class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtracking(nums, used, [], result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return  # 因为是在叶子节点收集需要的结果，因此需要return
        
        for i in range(len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, used, path, result)
            used[i] = False
            path.pop()            
        
