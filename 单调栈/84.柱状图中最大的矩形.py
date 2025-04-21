# 方法1: 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        思路：找每个柱子左右两侧第一个高度小于当前柱子的柱子
        栈顶到栈底：从大到小（每插入一个新的小数值时，都要弹出先前的大数值）
        栈顶，栈顶的下一个元素，即将入栈的元素：这三个元组组成了最大面积的高度和宽度
        情况1: 当前遍历的元素heights[i]大于栈顶元素
        情况2: 当前遍历的元素heights[i]等于栈顶元素
        情况3: 当前遍历的元素heights[i]小于栈顶元素
        """

        # 输入数组首尾各补0
        heights.insert(0, 0)
        heights.append(0)

        stack = [0]
        res = 0
        
        for i in range(1, len(heights)):
            # 情况1
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            # 情况2
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # 情况3
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈顶是中间的柱子
                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        w = right_index - left_index - 1
                        h = heights[mid_index]
                        res = max(res, w * h)
                stack.append(i)
        return res
