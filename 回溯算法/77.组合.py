# 未剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] # 结果集
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:]) # path[:] 是path的浅拷贝
            return

        for i in range(start_index, n + 1):
            path.append(i) # 处理节点
            self.backtracking(n, k, i+1, path, result)
            path.pop() # 回溯

# 剪枝优化
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [] # 结果集
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start_index, n - (k - len(path)) + 2): # 剪枝优化
            path.append(i) # 处理节点
            self.backtracking(n, k, i+1, path, result)
            path.pop() # 回溯
