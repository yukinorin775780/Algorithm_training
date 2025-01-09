class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                cur = queue.popleft()
                level.append(cur.val)
                
                for child in cur.children: # 循环遍历当前节点的每个子节点加入下一层
                    queue.append(child)
            
            result.append(level)
        
        return result
