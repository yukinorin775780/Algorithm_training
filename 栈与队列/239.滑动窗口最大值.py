# 自定义的单调队列类
from collections import deque

class MyQueue: # 单调队列(从大到小)
    def __init__(self):
        self.queue = deque() # 需要使用deque实现单调队列，直接使用list会超时
    
    # 每次弹出时，比较当前要弹出的数值是否等于队列的出口元素的数值，如果相等则弹出
    # 同时pop前要判断队列当前是否为空
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft() # list.pop()时间复杂度为O(n),这里需要使用collections.deque()
    
    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止
    # 这样就保持了队列里的数值时单调递减 从大到小
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    # 返回队列最大值
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k): # 先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front()) # 记录前k元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i-k]) # 滑动窗口移除最前面的元素
            que.push(nums[i]) # 滑动窗口加入元素
            result.append(que.front()) # 记录对应的最大值
        return result

# 直接使用deque
from collections import deque

def update_que(que, num):
    # 移除所有小于新元素的队列尾部元素
    while que and num > que[-1]:
        que.pop()
    que.append(num)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        que = deque() # 单调队列
        
        for i in range(len(nums)):
            update_que(que,nums[i]) # 新元素加入

            if i >= k and nums[i-k] == que[0]: # 滑动窗口移除最前面的元素 = 单调队列头元素，需要移除头元素
                que.popleft()
            
            # 记录对应的最大值
            if i >= k-1:
                result.append(que[0])
        
        return result
            

