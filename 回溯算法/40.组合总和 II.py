# used数组实现去重逻辑
class Solution:
    def backtracking(self, candidates, target, sum, start_index, used, path, result):
        if sum == target:
            result.append(path[:])
            return
        
        for i in range(start_index, len(candidates)):
            # 对于相同的数字，只选择第一个未使用的数组，跳过其他相同的数字来实现去重逻辑
            if i > start_index and candidates[i] == candidates[i-1] and not used[i-1]:
                continue
            
            if sum + candidates[i] > target:
                break
            
            sum += candidates[i]
            path.append(candidates[i])
            used[i] = True
            self.backtracking(candidates, target, sum, i+1, used, path, result)
            # 回溯
            used[i] = False
            sum -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used = [False] * len(candidates)
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, used, [], result)
        return result

# 不使用used数组
class Solution:
    def backtracking(self, candidates, target, sum, start_index, path, result):
        if sum == target:
            result.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            
            if sum + candidates[i] > target:
                break
            
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, sum, i+1, path, result)
            sum -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

# 回溯优化
class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i + 1, path, result)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result
