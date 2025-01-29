class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result
    
    def backtracking(self, nums, start_index, path, result):
        result.append(path[:])  # 收集子集，要放在终止条件的上面，否则会漏掉自己
        if start_index >= len(nums): # 可以不加终止条件
            return
        
        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
