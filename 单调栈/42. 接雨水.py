class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈是按照 行 的方向来计算雨水
        从栈顶到栈底的顺序：从小到大
        通过 3 个元素来接雨水：栈顶，栈顶的下一个元素，以及即将入栈的元素
        雨水的高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
        雨水的宽度是 凹槽右边的下标 - 凹槽左边下标 - 1 (因为只求中间宽度)
        """

        stack = [0]
        res = 0
        for i in range(1, len(height)):
            # 情况1
            if height[i] < height[stack[-1]]:
                stack.append(i)
            # 情况2
            # 当 当前柱子的高度和栈顶高度一致时，左边的柱子不能存放雨水，所以只保留右边的柱子
            # 需要使用最右边的柱子来计算宽度
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)

            # 情况3
            else:
                # 抛出所有比当前柱子低的柱子
                while stack and height[i] > height[stack[-1]]:
                    # 栈顶就是中间柱子，是凹糟的底部
                    mid_height = height[stack[-1]]
                    stack.pop()
                    if stack:
                        right_height = height[i]
                        left_height = height[stack[-1]]
                        # 两侧较矮的一方作为高度
                        h = min(left_height, right_height) - mid_height
                        # 宽度是凹槽右边的下标 - 凹槽左边下标 - 1 (因为只求中间宽度)
                        w = i - stack[-1] - 1
                        # 体积
                        res += h * w
                stack.append(i)
        
        return res


# 暴力
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            l_height = height[i-1]
            r_height = height[i+1]
            for j in range(i-1):
                if height[j] > l_height:
                    l_height = height[j]
            for k in range(i+2, len(height)):
                if height[k] > r_height:
                    r_height = height[k]
            res1 = min(l_height, r_height) - height[i]
            if res1 > 0:
                res += res1
        return res
