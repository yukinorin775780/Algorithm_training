# 小饼干满足小胃口的孩子
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # 将小孩按胃口大小排序
        s.sort()    # 将饼干按尺寸大小排序
        index = 0
        result = 0
        for i in range(len(g)): # 遍历小孩
            if index < len(s) and s[index] >= g[i]: # 饼干尺寸大于小孩胃口
                result += 1
                index += 1
        return result
