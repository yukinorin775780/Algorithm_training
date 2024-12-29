# 使用数组1（自己想的）
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = [0] * 26
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        for c in ransomNote:
            magazine_count[ord(c) - ord('a')] -= 1
        for i in range(26):
            if magazine_count[i] < 0:
                return False
        return True 

# 使用数组2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))

# 使用defaultdict
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1
        
        for x in ransomNote:
            value = hashmap.get(x)
            # value 为 0 或 None，表示 magazine 中没有足够的字符来构造 ransomNote
            if not value:
                return False
            else:
                hashmap[x] -= 1

        return True

# 使用字典
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1
        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True

# 使用 Counter
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)

# 使用 count + 精简
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))

# 使用 count + 简单易懂
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine and ransomNote.count(char) <= magazine.count(char):
                continue
            else:
                return False
        return True
        
