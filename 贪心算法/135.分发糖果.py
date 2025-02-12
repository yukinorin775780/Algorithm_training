class Solution:
    def candy(self, ratings: List[int]) -> int:
        sweets = [1] * len(ratings)
        # 右孩子得分大于左孩子
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                sweets[i] = sweets[i-1] + 1

        # 左孩子得分大于右孩子
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                sweets[i] = max(sweets[i+1]+1, sweets[i])
        
        return sum(sweets)
