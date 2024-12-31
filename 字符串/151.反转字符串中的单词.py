# 方法1
class Solution:
    def reverseWords(self, s: str) -> str:
        # 删除前后空白
        s = s.strip()
        # 翻转整个字符串
        s = s[::-1]
        # 将字符串拆分成单词，并翻转每个单词
        s = ' '.join(word[::-1] for word in s.split())
        return s

# 方法2
class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分成单词，即转换为列表类型
        words = s.split()
        
        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        # 将列表转换为字符串
        return " ".join(words)

# 方法3 
class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分成单词，即转换为列表类型
        words = s.split()
        # 反转单词
        words = words[::-1]
        # 列表转字符串
        return " ".join(words)
