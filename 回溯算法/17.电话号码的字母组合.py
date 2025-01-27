class Solution:
    def __init__(self):
        self.letter_map = [
            "",     #0
            "",     #1
            "abc",  #2
            "def",  #3
            "ghi",  #4 
            "jkl",  #5
            "mno",  #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9
        ]
        self.result = []
        self.s = ""
    
    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])  # 将索引处的数字转换为整数
        letters = self.letter_map[digit]    # 获取对应字符集
        for i in range(len(letters)):
            self.s += letters[i]    # 处理字符
            self.backtracking(digits, index + 1)
            self.s = self.s[:-1] # 回溯，删除最后添加的字符

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result


# 回溯精简版1
class Solution:
    def __init__(self):
        self.letter_map = [
            "",     #0
            "",     #1
            "abc",  #2
            "def",  #3
            "ghi",  #4 
            "jkl",  #5
            "mno",  #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9
        ]
        self.result = []

    def getCombinations(self, digits, index, s):
        if index == len(digits):
            self.result.append(s)
            return
        digit = int(digits[index])  # 将索引处的数字转换为整数
        letters = self.letter_map[digit]    # 获取对应字符集
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.getCombinations(digits, 0, "")
        return self.result

#回溯精简版2
class Solution:
    def __init__(self):
        self.letter_map = [
            "",     #0
            "",     #1
            "abc",  #2
            "def",  #3
            "ghi",  #4 
            "jkl",  #5
            "mno",  #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9
        ]

    def getCombinations(self, digits, index, s, result):
        if index == len(digits):
            result.append(s)
            return
        digit = int(digits[index])  # 将索引处的数字转换为整数
        letters = self.letter_map[digit]    # 获取对应字符集
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter, result)

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        self.getCombinations(digits, 0, "", result)
        return result
