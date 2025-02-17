class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 0:
            return result   # 区间集合为空直接返回
        # 按照区间的左边界进行排序    
        intervals.sort(key=lambda x:x[0])
        # 第一个区间直接放入结果集中
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:    # 发现重叠区间
                result[-1][1] = max(result[-1][1], intervals[i][1]) # 更新结果区间右边界
            else:
                # 区间不重叠
                result.append(intervals[i]) 

        return result
