class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            prev = None
            
            for _ in range(size):
                cur = queue.popleft()
                
                if prev:
                    prev.next = cur
                
                prev = cur

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return root
