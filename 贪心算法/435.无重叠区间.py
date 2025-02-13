class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key= lambda x:x[0])
        result = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]: # 存在重叠区间
                result += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])   # 更新右边界
        
        return result
