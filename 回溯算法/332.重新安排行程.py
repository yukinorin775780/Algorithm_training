# 使用字典
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}

        # 根据航班每一站的重点字母排序
        tickets.sort(key=lambda x:x[1])

        # 罗列每一站的下一个可选项
        for u, v in tickets:
            if u in self.adj:
                self.adj[u].append(v)
            else:
                self.adj[u] = [v]
        
        # 从JFK出发
        self.result = []
        self.dfs("JFK")

        return self.result[::-1]
    
    def dfs(self, s):
        # 如果城市存在且有飞机能到另一城市
        while s in self.adj and len(self.adj[s]) > 0:
            # 找到s能到哪里，选能到的第一个机场
            v = self.adj[s][0]
            self.adj[s].pop(0)
            self.dfs(v)
        
        self.result.append(s)

#使用字典 逆序
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list) # 创建默认字典，用于存储机场映射关系
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])    # 将机票输入到字典里
        
        for key in targets:
            targets[key].sort(reverse = True)   # 对到达机场列表进行字母逆序排序
        
        result = []
        self.backtracking("JFK", targets, result)
        return result[::-1] # 返回逆序的行程路径

    def backtracking(self, airport, targets, result):
        while targets[airport]: # 当前机场存在可到达的机场
            next_airport = targets[airport].pop()   # 弹出下一个机场
            self.backtracking(next_airport, targets, result)
        result.append(airport)  # 将当前机场添加到行程路径
