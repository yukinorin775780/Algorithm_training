class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occr = {}  # 存醋每个字符最后出现的位置
        for i, ch in enumerate(s):
            last_occr[ch] = i
        
        result = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            # 当前字符出现的最远位置
            end = max(end, last_occr[ch])
            if i == end:    #如果当前位置已经是最远位置，表示可以分割出一个区间
                result.append(end-start+1)
                start = i + 1
        
        return result
