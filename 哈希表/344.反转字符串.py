# 使用双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# 使用栈
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        for i in range(len(s)):
            s[i] = stack.pop()

# 使用 range
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n-i-1] = s[n-i-1], s[i]

# 使用 reversed
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = reversed(s)

# 使用切片
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

# 使用列表推导
class Solution:
  def reverseString(self, s: List[str]) -> None:
      s[:] = [s[i] for i in range(len(s)-1, -1, -1)]

# 使用 reverse()
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
