class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 0, 1, [], result)
        return result
    
    def backtracking(self, target_sum, k, sum, start_index, path, result):
        if sum > target_sum: # 剪枝操作1
            return
        if len(path) == k: # 终止条件
            if sum == target_sum:
                result.append(path[:])
            return
        
        for i in range(start_index, 9 - (k - len(path)) + 2): # 剪枝操作2
            sum += i
            path.append(i)
            self.backtracking(target_sum, k, sum, i+1, path, result)
            sum -= i
            path.pop()
