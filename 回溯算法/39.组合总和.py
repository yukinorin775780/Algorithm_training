# 回溯版本1
class Solution:
    def backtracking(self, candidates, target, sum, start_index, path, result):
        if sum > target:
            return
        if sum == target:
            result.append(path[:])
            return
        
        for i in range(start_index, len(candidates)):
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, sum, i, path, result)
            sum -= candidates[i]
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

# 回溯版本1 + 剪枝
class Solution:
    def backtracking(self, candidates, target, sum, start_index, path, result):
        if sum == target:
            result.append(path[:])
            return
        
        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                break
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, sum, i, path, result)
            sum -= candidates[i]
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result
      
# 回溯版本2
class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, path, result)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result

# 回溯版本2 + 剪枝
class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start_index, len(candidates)):
            if target - candidates[i] < 0:
                break
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, path, result)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, [], result)
        return result
