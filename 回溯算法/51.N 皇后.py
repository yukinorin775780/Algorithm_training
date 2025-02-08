class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = [] # 存储最终结果的二维字符串数组

        chessboard = ['.' * n for _ in range(n)]    # 初始化棋盘
        self.backtracking(n, 0, chessboard, result)
        return [[''.join(row) for row in solution] for solution in result]

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])    # 棋盘填满，将当前结果加入结果集
            return
        
        for col in range(n):
            if self.isVaild(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:] # 放置皇后
                self.backtracking(n, row+1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:] # 回溯
    
    def isVaild(self, row, col, chessboard) -> bool:
        # 检查列
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        
        # 检查45度
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
