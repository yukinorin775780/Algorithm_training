class MyQueue:

    def __init__(self):
        self.stack_in = [] # push
        self.stack_out = [] # pop

    def push(self, x: int) -> None:
        # 有新的元素进来，就往 in 里面 push
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
       
    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
