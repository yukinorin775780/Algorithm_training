class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0 # 起始点
        loop, mid = n // 2, n // 2 # 循环次数，n为奇数时，mid为矩阵的中心点
        count = 1 # 计数

        for offset in range(1, loop + 1): # 每一层循环偏移量+1，偏移量从1开始
            for i in range(starty, n - offset): # 从左到右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset): # 从上到下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1): # 从右到左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1): # 从下到上 
                nums[i][starty] = count
                count += 1
            startx += 1 # 更新起始点
            starty += 1
        
        if n % 2 != 0: # n为奇数时，填充中心点
            nums[mid][mid] = count

        return nums
