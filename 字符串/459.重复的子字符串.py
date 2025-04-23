# 方法1: 移动匹配
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1]
        # find返回的是找到几个，没找到返回-1
        return ss.find(s) != -1



# 方法2: KMP
class Solution:
    def getNext(self, next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
            next[i] = j
        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        next = [0] * len(s)
        self.getNext(next, s)
        if next[-1] != -1 and len(s) % (len(s) - (next[-1] + 1)) == 0:
            return True
        return False
