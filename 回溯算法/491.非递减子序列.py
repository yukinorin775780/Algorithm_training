# 回溯-利用set去重
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result
    
    def backtracking(self, nums, start_index, path, result):
        if len(path) > 1:
            result.append(path[:]) # 注意要使用切片将当前路径的副本加入结果集
        uset = set()    # 使用集合对本层元素进行去重
        for i in range(start_index, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:  # 不符合递增要求或本层已经出现过
                continue
            
            uset.add(nums[i])   # 记录本层使用过的元素
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()

# 回溯-利用hash表去重
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result
    
    def backtracking(self, nums, start_index, path, result):
        if len(path) > 1:
            result.append(path[:]) # 注意要使用切片将当前路径的副本加入结果集
        used = [0] * 201    # 使用数组去重，题目范围在[-100, 100]
        for i in range(start_index, len(nums)):
            if (path and nums[i] < path[-1]) or used[nums[i] + 100] == 1:  # 不符合递增要求或本层已经出现过
                continue
            
            used[nums[i] + 100] = 1   # 记录本层使用过的元素
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
