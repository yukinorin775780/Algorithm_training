# 小饼干满足小胃口的孩子
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # 将小孩按胃口大小排序
        s.sort()    # 将饼干按尺寸大小排序
        index = 0
        # result = 0
        for i in range(len(s)): # 遍历饼干
            if index < len(g) and g[index] <= s[i]: # 小孩胃口小于饼干尺寸
                # result += 1
                index += 1
        return result
