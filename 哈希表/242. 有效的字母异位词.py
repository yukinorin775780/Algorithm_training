class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            # 用来记录在 s 中出现过的字母
            record[ord(i) - ord("a")] += 1
        
        for i in t:
            # 用 t 中出现过的字母减去 s 出现过的字母
            record[ord(i) - ord("a")] -= 1
        
        for i in range(26):
            # 如果该数组中任意位置不为0，那么就说明不是字母异位词
            if record[i] != 0:
                return False
        return True
