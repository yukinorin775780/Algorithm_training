class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        1. 确定dp数组定义：dp[i][j]表示从（0 ，0）出发到(i, j) 有dp[i][j]条不同的路径。
        2. 确定递推公式: 无障碍时: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        3. dp数组初始化：无障碍时：dp[i][0] = 1,dp[j][0] = 1；有障碍后的dp[i][0],dp[0][j] = 0     
        4. 确定遍历顺序：从左到右从上到下
        5. 打印dp数组
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 初始位置 或 终止位置有障碍
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        # 创建dp数组
        dp = [[0] * n for _ in range(m)]
        # 初始化dp数组
        for i in range(m):
            # 遇到障碍物时直接退出循环，后面默认都是0
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            # 同理
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        # 递推
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
