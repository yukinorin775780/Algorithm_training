class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            # 当前元素 <= 栈顶元素时，入栈
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            # 当前元素 > 栈顶元素
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]  # stack存的是索引值
                    stack.pop()
                stack.append(i)

        return res
