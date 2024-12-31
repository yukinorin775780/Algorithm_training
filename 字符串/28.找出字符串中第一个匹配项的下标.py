# 暴力法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        return -1

# 使用 index
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

# 使用 find
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
