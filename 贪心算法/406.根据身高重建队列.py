class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照h维度的身高顺序从高到低排序，确认第一维度
        # lambda返回的是一个元组：当 -x[0](维度h)相同时，再根据x[1](维度k)从小到大排序
        people.sort(key=lambda x:(-x[0], x[1]))
        que = []
        # 根据每个元素的第二个维度k进行排序
        for p in people:
            que.insert(p[1], p)
        return que
