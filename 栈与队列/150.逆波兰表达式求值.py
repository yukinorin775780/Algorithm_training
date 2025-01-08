from operator import add, sub, mul

def div(x,y):
    # 使用整数除法的向零取整方式
    return int(x/y) if x*y > 0 else -(abs(x) // abs(y))

class Solution:
    op_map = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.op_map[token](a, b))
        return stack.pop()
