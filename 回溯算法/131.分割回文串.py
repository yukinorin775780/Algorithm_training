# 回溯 基本版
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, start_index, path, result):
        # 终止逻辑
        if start_index == len(s):
            result.append(path[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 判断被截取的子串s[start_index, i]是否为回文串
            if self.isPalindrome(s, start_index, i):
                path.append(s[start_index: i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def isPalindrome(self, s, start, end) -> bool:
        i: int = start
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# 回溯 + 优化判定回文函数
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, start_index, path, result):
        # 终止逻辑
        if start_index == len(s):
            result.append(path[:])
            return
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 若正序和倒序相同，则是回文串
            if s[start_index : i + 1] == s[start_index : i + 1][::-1]:
                path.append(s[start_index: i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

# 回溯 + 高效判断回文子串 - 动态规划
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        isPalindrome = [[False] * len(s) for _ in range(len(s))]
        self.computePalinerome(s, isPalindrome)
        self.backtracking(s, 0, [], result, isPalindrome)
        return result
    
    def backtracking(self, s, start_index, path, result, isPalindrome):
        # 终止逻辑
        if start_index >= len(s):
            result.append(path[:])
            return

        # 单层递归逻辑
        for i in range(start_index, len(s)):
            if isPalindrome[start_index][i]: # 是回文串
                sub_string = s[start_index : i + 1]
                path.append(sub_string)
                self.backtracking(s, i+1, path, result, isPalindrome)
                path.pop()
    
    def computePalinerome(self, s, isPalindrome):
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j == i:
                    isPalindrome[i][j] = True
                elif j - i == 1:
                    isPalindrome[i][j] = (s[i] == s[j])
                else:
                    isPalindrome[i][j] = (s[i] == s[j] and isPalindrome[i+1][j-1])

# 回溯 + 使用 all 函数判断回文子串
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, start_index, path, result):
        # 终止逻辑
        if start_index == len(s):
            result.append(path[:])
            return

        # 单层递归逻辑
        for i in range(start_index + 1, len(s) + 1):
            sub = s[start_index : i]
            if self.isPalindrome(sub):
                path.append(sub)
                self.backtracking(s, i, path, result)
                path.pop()
    
    def isPalindrome(self, s):
        return all(s[i] == s[len(s) - 1 - i] for i in range(len(s) // 2))
