class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda x:x[0])
        result = 1
        for i in range(1, len(points)):
            # 当前气球和上一个气球没有重叠区域
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                # 更新重叠气球的最小右边界
                points[i][1] = min(points[i-1][1], points[i][1])
        
        return result
