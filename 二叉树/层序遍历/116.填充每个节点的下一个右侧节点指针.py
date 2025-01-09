class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = collections.deque([root])

        while queue:
            size = len(queue)
            prev = None # 记录上一个节点

            for _ in range(size):
                cur = queue.popleft()

                if prev:
                    prev.next = cur # 上一个节点指向当前节点
                
                prev = cur # 记录当前节点为上一个节点

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
        return root
